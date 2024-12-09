# README

# 🎙️ **Whisper Transcription Tool**

Transform your audio and video files into accurate subtitles with Whisper Transcription Tool. Designed for simplicity and versatility, this console application allows you to transcribe or translate content, with options for models, languages, and output formats.

---

## 🚀 **Key Features**

* **Transcription or Translation** : Convert audio into text or translate it into another language.
* **Interactive Menus** : Intuitive interface with options for models, output formats, and languages.
* **Whisper Models** : Choose from `tiny`, `base`, `small`, `medium`, or `large` for performance tailored to your needs.
* **Language Flexibility** : Supports multiple languages including English, Spanish, French, German, Chinese, and more.
* **Rich Outputs** : Generate subtitles in formats like `.txt`, `.srt`, `.json`, or all at once.

---

## 📸 **Demo**

### **Main Workflow**

1. **File Selection**

   ![File selection illustration](https://portfoliotavm.com/imagevscode/1.mp4)

   Choose the audio or video file you want to process.
2. **Model & Task Selection**

   ![Task and model selection illustration](https://portfoliotavm.com/imagevscode/2.mp4)

   Pick the Whisper model and task (`Transcribe` or `Translate`) through a menu.
3. **Output Language and Format**

   ![Output settings illustration](https://portfoliotavm.com/imagevscode/3.mp4)

   Select the language and the desired subtitle format.
4. **Result**
 

   Your subtitles are ready in the output directory!

---

## 🛠️ **Installation**

### **Prerequisites**

* Python 3.8 or higher
* Pip (Python package manager)

### **Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/VMASPAD/whisappsg.git
   cd whisper-transcription-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```bash
   python main.py
   ```

---

## 📋 **Usage Instructions**

1. Run the tool:
   ```bash
   python transcriber.py
   ```
2. Follow the on-screen interactive menus to:
   * Select your audio/video file.
   * Choose the transcription task (`transcribe` or `translate`).
   * Pick a model, output format, and language.
   * Save your subtitles to a chosen directory.
3. Wait for the process to complete, and find your subtitles in the specified output folder.

---

## 🌎 **Supported Languages**

* **English**
* **Spanish**
* **French**
* **German**
* **Chinese**
* ...and many more!

---

## 🖥️ **Preview**

**Sample Output (English - SRT format):**

```srt
1  
00:00:00,000 --> 00:00:03,000  
Welcome to the Whisper transcription tool.  

2  
00:00:03,001 --> 00:00:06,500  
This tool converts your audio files into text effortlessly.
```

**Translated Output (Spanish - TXT format):**

```txt
Bienvenido a la herramienta de transcripción Whisper.  
Esta herramienta convierte tus archivos de audio en texto sin esfuerzo.
```

---

## ✨ **Why Choose Whisper Transcription Tool?**

* **Accurate Results** : Leverage OpenAI's Whisper models for state-of-the-art transcription.
* **Customizable** : Choose tasks, languages, models, and formats as per your project needs.
* **Efficient Workflow** : Seamless interaction through intuitive menus.

---

## 📞 **Support**

If you have any issues, suggestions, or feedback, feel free to open an issue on the [GitHub repository](https://github.com/yourusername/whisper-transcription-tool/issues).

---

## 🏆 **Contribute**

Want to enhance the tool?

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a pull request.
