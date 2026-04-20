# Adversarial Vulnerabilities in AI Perception: Evaluating Multimodal LLM Fallibility to Classic Visual Illusions

**Independent Research Project**  
**Intersection of Computer Vision & Cognitive Psychology**

## Abstract
This repository contains a programmatic framework to evaluate whether Large Language Models (LLMs) with vision capabilities "see" the world using human-like cognitive heuristics or if they process geometry through objective mathematical measurement. 

By testing four distinct Gemini model architectures against a controlled dataset of classic optical illusions (**Müller-Lyer, Ponzo, and Ebbinghaus**), this study identifies a correlation between model parameter density and objective perception. The results suggest that smaller multimodal models exhibit "human-like" heuristic vulnerabilities, while larger models demonstrate a move toward objective geometric analysis.

## Methodology

### 1. Programmatic Stimulus Generation (`01_generate_illusions.py`)
In cognitive science research, image artifacts can act as confounding variables. To ensure absolute control, this project utilizes a custom Python script to generate visual stimuli from scratch using `Matplotlib` and `NumPy`.
* **Standardization:** In all 30 generated test cases, **Target B** is physically identical to **Target A** but is surrounded by contextual cues that trigger human illusory perception of increased size/length.
* **Variety:** The dataset includes 10 Müller-Lyer (lines with fins), 10 Ponzo (converging tracks), and 10 Ebbinghaus (contextual circles) illusions.

### 2. Automated API Evaluation (`02_run_illusion_test.py`)
The study utilizes a zero-shot, deterministic evaluation pipeline:
* **Models Tested:** `gemini-3-flash-preview`, `gemini-2.5-flash`, `gemini-3.1-flash-lite-preview`, and `gemini-2.5-flash-lite`.
* **Prompt Engineering:** The models were instructed to compare A and B and reply strictly with one word ('A', 'B', or 'Same'). 
* **Control:** Temperature was set to `0.0` to ensure deterministic, highest-probability outputs.
* **Data Ingestion:** Results were logged in real-time to a structured `.csv` file for statistical analysis.

### 3. Data Analysis (`03_visualize_illusions.py`)
The final phase utilizes `Pandas` and `Seaborn` to ingest the CSV data and generate a stacked bar chart, visualizing the susceptibility of each model to the illusions.

## Key Findings
* **Objective Perception:** The larger models (`3-flash`, `2.5-flash`, `3.1-flash-lite`) demonstrated nearly 100% accuracy, correctly identifying that Target A and Target B were the "Same" length/size. They functioned as mathematical pixel-measurers rather than heuristic observers.
* **Heuristic Vulnerability:** The smallest model (`2.5-flash-lite`) was the most susceptible to the illusions, choosing the "human-like" incorrect answer (Target B) or committing errors (Target A) in approximately **90% of test cases**.
* **Cognitive Scaling:** The data suggests that as multimodal models scale down in parameters, they rely more heavily on visual heuristics similar to human "fast-thinking" perception, whereas larger models possess the capacity for deeper geometric reasoning.

## Repository Structure
```text
├── data/                               
│   ├── illusion_dataset/               # 30 programmatically generated PNG stimuli
│   └── illusion_results.csv            # Final aggregated model response data
├── results/                            
│   └── illusion_results_expanded.png   # Visualization of model performance vs. illusions
├── scripts/                            
│   ├── 01_generate_illusions.py        # Generates standardized visual stimuli
│   ├── 02_run_illusion_test.py         # Multi-model API testing suite
│   └── 03_visualize_illusions.py       # Statistics and visualization generator
└── paper/                              
    └── visual_perception_paper_draft.md # Formal academic write-up
```

## Technologies Used
* **Python 3.12**
* **Google Generative AI SDK** (Multimodal LLM testing)
* **Matplotlib / NumPy** (Stimulus generation)
* **Pandas** (Data manipulation)
* **Pillow** (Image processing)
