
from config import save_config, load_config, config
from ai import ask_ai_stream
import os
import random
from ui import (
    console,
    show_dashboard,
    show_help,
    show_about,
    show_config,
    show_stats,
    show_stats_status,
    show_reset,
    show_version,
    status,
    show_success,
    show_warning,
    show_error,
    show_theme,
    show_history,
    show_usage,
    show_models,
    show_current_model,
    show_search_results,
    show_update,
    confirm_exit,
    goodbye,
    show_documents,
    show_document_info,
    show_docs_help,
    show_document_sources,
)
from setup import is_first_run, run_setup
from theme import get_theme, get_theme_icon, get_theme_name, set_theme, list_themes
from storage import save_chat
from storage import list_chats, load_chat, list_chats, delete_chat, rename_chat
from models import list_models, current_model, set_model, model_exists, suggest_models
from exporter import export_markdown, export_text, export_pdf
from search import search_current
from updater import is_update_available
from documents import load_documents, remove_document, clear_documents, get_document
from rag import index_document, ask_document
from documents import initialize as initialize_documents
from vectors import initialize as initialize_vectors
initialize_documents()
initialize_vectors()
from vectors import delete_document, clear_database, get_chunk_count
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

stats_enabled = False
document_chat = False

def get_doc_status():
    docs = load_documents()
    count = len(docs)
    active = config.get("active_documents")
    if active is None:
        active_text = "All" if count > 0 else "None"
    elif len(active) == 0:
        active_text = "None"
    else:
        active_text = str(len(active))
    return count, active_text

def main():
    global stats_enabled
    global document_chat
    
    if is_first_run():
        config = run_setup()

        if config is None:
            return

    config = load_config()

    clear_screen()
    set_theme(config.get("theme", "default"))
    doc_count, active_text = get_doc_status()
    show_dashboard(stats_enabled, document_chat, doc_count, active_text)

    history = []
    while True:
            print()
            prompt = input("You > ")

            if not prompt.strip():
                continue
            
            if prompt.lower() == "/bye":
                show_success("Goodbye! 👋")
                break

            if prompt.lower() == "/stats":
                show_stats_status(stats_enabled)
                continue
            
            if prompt.lower() == "/history":
                files = list_chats()
                show_history(files)
                continue
            
            if prompt.lower() == "/docs chat on":
                document_chat = True
                clear_screen()
                doc_count, active_text = get_doc_status()
                show_dashboard(stats_enabled, document_chat, doc_count, active_text)
                show_success("📚 Document Chat Enabled")
                continue

            if prompt.lower() == "/docs chat off":
                document_chat = False
                clear_screen()
                doc_count, active_text = get_doc_status()
                show_dashboard(stats_enabled, document_chat, doc_count, active_text)
                show_success("📚 Document Chat Disabled")
                continue

            elif prompt.lower().startswith("/docs use "):
                argument = prompt[10:].strip()

                if argument.lower() == "all":
                    config["active_documents"] = None

                elif argument.lower() == "none":
                    config["active_documents"] = []

                else:
                    try:
                        document_ids = []

                        for value in argument.split():
                            document_ids.append(int(value))

                    except ValueError:
                        show_warning(
                            "Invalid document ID.\n\n"
                            "Usage: /docs use <id1> <id2> ...\n"
                            "Example: /docs use 1 3 5"
                        )
                        continue

                    documents = load_documents()
                    valid_ids = {doc["id"] for doc in documents}
                    invalid = [did for did in document_ids if did not in valid_ids]

                    if invalid:
                        show_warning(
                            f"Document ID(s) not found: {', '.join(str(i) for i in invalid)}\n\n"
                            "Use /docs list to see available documents."
                        )
                        continue

                    config["active_documents"] = document_ids

                save_config()

                active = config.get("active_documents")
                if active is None:
                    active_desc = "All documents"
                elif len(active) == 0:
                    active_desc = "No documents"
                else:
                    active_desc = ", ".join(str(i) for i in active)

                show_success(
                    f"Active documents updated.\n\n"
                    f"🎯 Active: {active_desc}"
                )

                continue

            elif prompt.lower().startswith("/docs remove "):
                argument = prompt[13:].strip()

                try:
                    document_id = int(argument)

                except ValueError:
                    show_warning(
                        "Invalid document ID.\n\n"
                        "Usage: /docs remove <id>"
                    )
                    continue

                success, result = remove_document(document_id)

                if not success:
                    show_warning(result)
                    continue

                try:
                    delete_document(document_id)
                except Exception:
                    pass

                active = config.get("active_documents")
                if active is not None and document_id in active:
                    active.remove(document_id)
                    save_config()

                show_success(
                    f"Document removed.\n\n"
                    f"📄 {result['name']}"
                )

                continue

            elif prompt.lower() == "/docs clear":
                documents = load_documents()

                if not documents:
                    show_warning("No documents to clear.")
                    continue

                show_warning(
                    f"⚠️ This will delete all {len(documents)} indexed document(s) and their vectors."
                )

                confirm = input("\nContinue? (y/N) > ").strip().lower()

                if confirm != "y":
                    show_success("Operation cancelled.")
                    continue

                clear_documents()
                clear_database()

                config["active_documents"] = None
                save_config()

                show_success(
                    f"All documents removed.\n\n"
                    f"🗑️ Deleted: {len(documents)} document(s)"
                )

                continue

            if prompt.lower() == "/docs list":
                documents = load_documents()
                active_ids = config.get("active_documents")
                show_documents(documents, active_ids)
                continue

            if prompt.lower().startswith("/docs info "):
                argument = prompt[11:].strip()

                try:
                    document_id = int(argument)
                except ValueError:
                    show_warning(
                        "Invalid document ID.\n\n"
                        "Usage: /docs info <id>"
                    )
                    continue

                document = get_document(document_id)

                if document is None:
                    show_warning(
                        f"Document with ID {document_id} not found.\n\n"
                        "Use /docs list to see available documents."
                    )
                    continue

                chunk_count = get_chunk_count(document_id)

                active = config.get("active_documents")
                is_active = active is None or document_id in (active or [])

                show_document_info(document, chunk_count, is_active)
                continue

            if prompt.lower().startswith("/docs add "):
                path = prompt[10:].strip().strip('"')

                try:
                    with console.status("📄 Indexing document...", spinner="dots"):
                        document_id = index_document(path)

                    document = get_document(document_id)
                    chunk_count = get_chunk_count(document_id)

                    show_success(
                        f"Document indexed successfully.\n\n"
                        f"🆔 ID: {document_id}\n"
                        f"📄 Name: {document['name']}\n"
                        f"📦 Chunks: {chunk_count}"
                    )

                except Exception as error:
                    show_error(str(error))

                continue

            if prompt.lower() in ("/docs", "/docs help"):
                show_docs_help()
                continue

            if prompt.lower() == "/search":
                show_usage(
                    "/search",
                    [
                        "/search <text>",
                    ],
                    "/search python"
                )
                continue
            
            if prompt.lower().startswith("/search "):

                query = prompt.split(maxsplit=1)[1]

                results = search_current(history, query)

                show_search_results(results, query)

                continue
                        
            if prompt.lower().startswith("/delete "):
                try:
                    index = int(prompt.split()[1])
                except:
                    show_warning("Usage: /delete <number>")
                    continue
                chat = delete_chat(index)
                if chat is None:
                    show_warning("Chat not found.")
                else:
                    show_success(
                        f"Deleted '{chat['title']}'"
                    )
                continue
            
            if prompt.lower() == "/models":
                models = list_models()
                show_models(models)
                continue
            
            if prompt.lower() == "/model":
                model = current_model()
                if isinstance(model, str):
                    show_error(model)
                else:
                    show_current_model(model)
                    continue

            if prompt.lower().startswith("/model "):
                old_model = config["model"]
                model_name = prompt.split(maxsplit=1)[1]
                if set_model(model_name):
                    show_success(f"✅ Active model updated\n\n"f"Previous:\n{old_model}\n\n"f"Current:\n{model_name}")
                else:
                    matches = suggest_models(model_name)

                    message = (
                        f"Model '{model_name}' isn't installed.\n\n"
                    )

                    if matches:
                        message += "Did you mean?\n\n"

                        for i, match in enumerate(matches, start=1):
                            message += f"[bold cyan]{i}.[/] {match}\n"
    
                    message += "\nUse /models to view installed models."

                    show_warning(message)
                continue
            
            if prompt.lower().startswith("/rename "):
                parts = prompt.split(maxsplit=2)
                if len(parts) < 3:
                    show_warning("Usage: /rename <number> <title>")
                    continue
                try:
                    index = int(parts[1])
                except ValueError:
                    show_warning("Usage: /rename <number> <title>")
                    continue

                new_title = parts[2]
                chat = rename_chat(index, new_title)
                if chat is None:
                    show_warning("Chat not found.")
                else:
                    show_success(
                        f"Renamed to '{new_title}'"
                    )
                continue
                
            if prompt.lower() == "/delete":
                show_usage(
                    "/delete",
                    "/delete <number>",
                    "/delete 1"
                )
                continue
            
            if prompt.lower() == "/load":
                show_usage(
                    "/load",
                    "/load <number>",
                    "/load 2"
                )
                continue
            
            if prompt.lower() == "/rename":
                show_usage(
                    "/rename",
                    "/rename <number> <new title>",
                    "/rename 1 Python Notes"
                )
                continue
            
            if prompt.lower() == "/update":
                available, current, latest = is_update_available()
                show_update(current, latest, available)
                continue
                
            if prompt.lower().startswith("/load "):
                try:
                    index = int(prompt.split()[1])
                except:
                    show_warning("Usage: /load <number>")
                    continue
                
                chat = load_chat(index)
                if chat is None:
                    show_warning("Chat not found.")
                    continue
                history = chat["messages"]
                show_success(f"Loaded '{chat['title']}'")                   
                continue
                
            if prompt.lower() == "/save":

                if not history:
                    show_warning("Nothing to save yet.")
                    continue

                filename = save_chat(history)
                show_success(
                    f"Conversation saved.\n\n"
                    f"📁 chats/\n"
                    f"📄 {filename}"
                )
                continue
            
            if prompt.lower() == "/export":
                show_usage(
                    "/export",
                    [
                        "/export md",
                        "/export txt",
                        "/export pdf",
                    ],
                    "/export md",
                )
                continue

            if prompt.lower().startswith("/export "):

                option = prompt.split(maxsplit=1)[1].lower()

                if not history:
                    show_warning("Nothing to export yet.")
                    continue

                if option == "md":

                    file_path = export_markdown(history)

                    show_success(
                        "✅ Conversation Exported\n\n"
                        "📄 Format : Markdown (.md)\n"
                        f"📁 Folder : {file_path.parent}\n"
                        f"📄 File   : {file_path.name}\n"
                        f"💬 Messages : {len(history)}"
                    )

                elif option == "txt":

                    file_path = export_text(history)

                    show_success(
                        "✅ Conversation Exported\n\n"
                        "📄 Format : Plain Text (.txt)\n"
                        f"📁 Folder : {file_path.parent}\n"
                        f"📄 File   : {file_path.name}\n"
                        f"💬 Messages : {len(history)}"
                    )

                elif option == "pdf":
                    
                    file_path = export_pdf(history)

                    show_success(
                        "✅ Conversation Exported\n\n"
                        "📄 Format : PDF (.pdf)\n"
                        f"📁 Folder : {file_path.parent}\n"
                        f"📄 File   : {file_path.name}\n"
                        f"💬 Messages : {len(history)}"
                    )
                
                else:

                    show_warning(
                        "Unsupported format.\n\n"
                        "Supported formats:\n"
                        "• md\n"
                        "• txt\n"
                        "• pdf"
                    )
                    
                continue
            
            if prompt.lower() == "/help":
                show_help()
                continue
            
            if prompt.lower() == "/about":
                show_about()
                continue
            
            if prompt.lower() == "/theme":
                show_theme()
                continue
            
            if prompt.lower().startswith("/theme "):
                theme_name = prompt.split(maxsplit=1)[1].lower()

                if set_theme(theme_name):
                    config["theme"] = theme_name
                    save_config()
                    show_success(
                        f"Theme changed to {get_theme_icon()} {get_theme_name()}."
                    )
                else:
                    show_warning(
                        f"Unknown theme '{theme_name}'. Use /theme to see available themes."
                    )
                continue
            
            if prompt.lower() == "/reset":
                history.clear()
                show_reset()
                continue
            
            if prompt.lower() == "/version":
                show_version()
                continue

            if prompt.lower() == "/clear":
                clear_screen()
                doc_count, active_text = get_doc_status()
                show_dashboard(stats_enabled, document_chat, doc_count, active_text)
                continue

            if prompt.lower() == "/stats on":
                stats_enabled = True
                show_stats_status(stats_enabled)
                continue

            if prompt.lower() == "/stats off":
                stats_enabled = False
                show_stats_status(stats_enabled)
                continue
            
            if prompt.lower() == "/config":
                doc_count, active_text = get_doc_status()
                show_config(stats_enabled, document_chat, doc_count, active_text)
                continue
            
            history.append({
                "role": "user",
                "content": prompt,
            })

            sources = []

            if document_chat:
                response_stream, sources = ask_document(prompt)
            else:
                response_stream = ask_ai_stream(history)
                
            print()
            print(status(), end="", flush=True)

            full_response = ""
            stats = None

            first_chunk = True

            for event in response_stream:

                if "error" in event:
                    show_error(event["error"])
                    break

                if not event["done"]:

                    if first_chunk:
                        print("\r" + " " * 100, end="\r")
                        print("🤖 PocketAI >", end=" ", flush=True)
                        first_chunk = False

                    print(event["chunk"], end="", flush=True)
                    full_response += event["chunk"]

                else:
                    stats = event["stats"]

            print()

            if full_response:
                print()
                
                history.append({
                    "role": "assistant",
                    "content": full_response
                })

            if sources:
                show_document_sources(sources)

            if stats_enabled and stats:
                show_stats(stats)

if __name__ == "__main__":
    while True:
        try:
            main()
            break

        except KeyboardInterrupt:
            clear_screen()
            if confirm_exit():
                clear_screen()
                goodbye()
                break
            clear_screen()