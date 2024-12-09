import whisper
import tkinter as tk
from tkinter import filedialog
from rich.console import Console
from rich.prompt import IntPrompt
import argparse
import os

console = Console()

def select_file():
    """Open a dialog to select an audio or video file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an audio/video file",
        filetypes=[("Audio/Video Files", "*.mp3 *.mp4 *.wav *.m4a *.ogg *.flac")]
    )
    return file_path

def select_output_directory():
    """Open a dialog to select an output directory."""
    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.askdirectory(title="Select the output directory")
    return output_path

def display_menu(options, prompt="Select an option:"):
    """Display an interactive menu using Rich."""
    console.print("\n[bold yellow]Available options:[/bold yellow]")
    for i, option in enumerate(options, start=1):
        console.print(f"[bold cyan]{i}[/bold cyan]. {option}")
    return IntPrompt.ask(f"[bold green]{prompt}[/bold green]", choices=[str(i) for i in range(1, len(options) + 1)])

def transcribe_file(args):
    if args.audio:
        file_path = args.audio[0]
    else:
        console.print("[bold yellow]Select the file to transcribe:[/bold yellow]")
        file_path = select_file()
    if not file_path:
        console.print("[bold red]No file selected. Exiting...[/bold red]")
        return
    
    if args.output_dir:
        output_dir = args.output_dir
    else:
        console.print("[bold yellow]Select the directory to save the subtitles:[/bold yellow]")
        output_dir = select_output_directory()
    if not output_dir:
        console.print("[bold red]No directory selected. Exiting...[/bold red]")
        return

    # Task selection
    tasks = ["transcribe", "translate"]
    task_choice = display_menu(tasks, "Select the task:")
    task = tasks[task_choice - 1]

    # Model selection
    models = ["tiny", "base", "small", "medium", "large"]
    model_choice = display_menu(models, "Select the model to use:")
    model_name = models[model_choice - 1]

    # Output format selection
    formats = ["txt", "srt", "json", "all"]
    format_choice = display_menu(formats, "Select the output format:")
    output_format = formats[format_choice - 1]

    # Language selection
    languages = ["en", "es", "fr", "de", "it", "ja", "zh", "ru", "pt", "ar"]
    language_display = {
        "en": "English",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "ja": "Japanese",
        "zh": "Chinese",
        "ru": "Russian",
        "pt": "Portuguese",
        "ar": "Arabic"
    }
    language_choice = display_menu([language_display[lang] for lang in languages], "Select the language for the subtitles:")
    language_code = languages[language_choice - 1]

    console.print(f"[bold cyan]Loading Whisper model '{model_name}'...[/bold cyan]")
    model = whisper.load_model(model_name)

    console.print(f"[bold green]Processing {file_path} with task '{task}'...[/bold green]")
    result = model.transcribe(file_path, task=task, language=language_code)

    output_path = os.path.join(output_dir, f"subtitles.{output_format}")
    console.print(f"[bold cyan]Saving subtitles to {output_path}...[/bold cyan]")
    with open(output_path, "w", encoding="utf-8") as f:
        if output_format == "txt":
            f.write(result["text"])
        else:
            f.write(result.get("text", ""))  # Extend logic as needed

    console.print("[bold green]Process completed successfully. Subtitles generated.[/bold green]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whisper-based transcription application")
    parser.add_argument("audio", nargs="*", help="Audio or video file to transcribe")
    parser.add_argument("--output_dir", type=str, help="Directory to save the subtitles")
    parser.add_argument("--task", choices=["transcribe", "translate"], help="Task to perform")
    parser.add_argument("--language", type=str, help="Language to use for transcription or translation")
    
    args = parser.parse_args()
    transcribe_file(args)
