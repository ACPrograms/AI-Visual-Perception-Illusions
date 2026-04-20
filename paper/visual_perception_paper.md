# Adversarial Vulnerabilities in AI Perception: Evaluating Multimodal LLM Susceptibility to Classic Human Visual Illusions

**Author:** Amar Chabli  
**Date:** April 2026  
**Institution:** Berkeley City College / Independent Research

## Abstract
The human visual system relies on ingrained heuristics to interpret geometric information, making it susceptible to well-documented optical illusions. This study investigates whether modern multimodal Large Language Models (LLMs) share these human-like perceptual biases or if they engage in objective geometric analysis. Four distinct Google Gemini architectures were evaluated against a programmatically generated dataset of 30 controlled visual stimuli, encompassing the Müller-Lyer, Ponzo, and Ebbinghaus illusions. Results show that larger, more advanced models (`gemini-3-flash-preview`, `gemini-2.5-flash`, `gemini-3.1-flash-lite-preview`) performed with 100% objectivity, correctly identifying the physical sameness of the targets. In stark contrast, the smaller `gemini-2.5-flash-lite` model exhibited a catastrophic failure, choosing the incorrect object in 90% of cases and demonstrating a consistent, non-human perceptual bias. This suggests that AI perception does not scale linearly and that computationally constrained models may possess unique adversarial vulnerabilities not found in human cognition.

---

## 1. Introduction
A fundamental question in cognitive science is whether artificial intelligence "thinks" like a human. While LLMs can mimic human language, the nature of their visual processing remains a "black box." The human visual system, for instance, is not a perfect camera; it is a predictive engine that uses contextual cues and heuristics to rapidly interpret the world. This efficiency, however, makes humans susceptible to optical illusions, where contextual information leads to incorrect perceptual judgments.

Classic illusions like the Müller-Lyer, Ponzo, and Ebbinghaus are powerful tools for probing the underlying mechanisms of a visual system. By presenting these mathematically-controlled stimuli to multimodal AIs, we can directly test for cognitive isomorphism: does the AI "see" the world like a human, or is its perception fundamentally alien? This study seeks to answer that question by comparing the performance of multiple AI architectures against these classic cognitive tests.

## 2. Methodology

### 2.1 Programmatic Stimulus Generation
To eliminate confounding variables from image compression or inconsistent formatting, all visual stimuli were programmatically generated using Python's `Matplotlib` and `NumPy` libraries.

*   **Dataset:** 30 high-resolution PNG images were created, comprising 10 instances of each of the following illusions:
    1.  **Müller-Lyer Illusion:** Two physically identical horizontal lines; one with inward-facing fins, the other with outward-facing fins.
    2.  **Ponzo Illusion:** Two physically identical horizontal lines placed between converging diagonal lines, resembling railroad tracks.
    3.  **Ebbinghaus Illusion:** Two physically identical central circles; one surrounded by large contextual circles, the other by small contextual circles.
*   **Standardization:** In every generated image, the target objects were labeled 'A' and 'B'. The physical size/length of A and B were identical. The contextual cues were always arranged such that a human observer would perceive **Target B as larger**.

### 2.2 Automated Model Evaluation
A Python-based pipeline was developed to test four distinct Google Gemini models against the 30-image dataset.
*   **Models Tested:**
    *   `gemini-3-flash-preview`
    *   `gemini-2.5-flash`
    *   `gemini-3.1-flash-lite-preview`
    *   `gemini-2.5-flash-lite`
*   **Prompting:** For each image, a zero-shot, deterministic prompt was used: *"Look at the primary objects (lines or central circles) labeled A and B. Which one is physically larger or longer? Reply strictly with one word: 'A', 'B', or 'Same'."*
*   **Control Parameters:** The API temperature was set to `0.0` to ensure the model produced its most probable, deterministic response. Rate-limiting was handled with a 2-second pause between calls.
*   **Data Logging:** All 120 responses (30 images x 4 models) were parsed and logged into a structured `.csv` file for final analysis.

## 3. Results

The analysis of the 120 API calls revealed a stark performance divide between the model architectures. The raw data is summarized below:

| Model | Same (Objective) | Chose B (Illusion) | Chose A (Error) | Other |
| :--- | :--- | :--- | :--- | :--- |
| gemini-3-flash-preview | 30 | 0 | 0 | 0 |
| gemini-2.5-flash | 30 | 0 | 0 | 0 |
| gemini-3.1-flash-lite-preview | 30 | 0 | 0 | 0 |
| gemini-2.5-flash-lite | 3 | 7 | 20 | 0 |

### 3.1 Objective Perception in Advanced Models
The three most advanced models demonstrated 100% objective accuracy. In all 30 test cases, they correctly identified that Targets A and B were physically the "Same." This indicates that their vision processing is not analogous to human perception but instead functions as a precise geometric measurement tool, impervious to contextual cues.

### 3.2 Systemic Perceptual Bias in the Smaller Model
The `gemini-2.5-flash-lite` model exhibited a catastrophic failure rate of 90%. Crucially, it did not consistently fall for the human illusion (choosing B). Instead, it demonstrated a strong and systematic bias towards choosing **Target A** (20 out of 30 responses)—the object a human perceives as *smaller*.

![Graph of Results](https://raw.githubusercontent.com/AmarChabli/ai-visual-perception-illusions/main/results/illusion_results_expanded.png)  
*Figure 1: Stacked bar chart showing the response distribution for each model architecture.*

## 4. Discussion

The perfect performance of the larger models disproves the hypothesis of simple cognitive isomorphism. Their visual systems are fundamentally computational, capable of ignoring the contextual "distractors" that fool the human brain.

The most significant finding, however, is the "reverse illusion" effect observed in the `gemini-2.5-flash-lite` model. Its consistent selection of the object perceived as smaller by humans suggests a unique, non-human adversarial vulnerability. A plausible hypothesis is that this smaller, computationally-constrained model's feature detectors are biased by spatial occupancy. The contextual cues designed to make 'B' look larger (e.g., small, numerous surrounding circles) may be interpreted by the model as "clutter," leading it to perceive the area containing 'B' as more crowded, and thus the target object 'B' itself as smaller. Conversely, the open space around 'A' (provided by large, distant circles) may lead it to perceive 'A' as larger.

This behavior is not a human-like heuristic; it is a distinctly *machinic* perceptual bias that emerges at a specific computational scale.

## 5. Conclusion

Multimodal LLMs do not "see" the world in a way that is analogous to human perception. While larger models demonstrate a capacity for objective, mathematical geometry, smaller architectures can exhibit profound and systematic perceptual biases. These biases are not necessarily human-like and can, as shown in this study, manifest as a "reverse illusion" effect. This highlights a critical area for future research in AI safety and cognitive science: understanding and mapping the unique adversarial vulnerabilities that emerge in AI systems at different scales, ensuring that their perception of the world aligns with our own in critical applications.

***

### References

1. Müller-Lyer, F. C. (1889). *Optische Urteilstäuschungen*. *Archiv für Anatomie und Physiologie, Physiologische Abteilung*, 2, 263–270.

2. Ponzo, M. (1911). *Intorno ad alcune illusioni nel campo delle sensazioni tattili sull'illusione di Aristotele e fenomeni analoghi*. *Archives Italiennes de Biologie*.

3. Ebbinghaus, H. (1902). *Grundzüge der Psychologie*. Leipzig: Veit & Co.

4. Yue, X., et al. (2026). "Seeing Is Believing? A Benchmark for Multimodal Large Language Models on Visual Illusions and Anomalies." *arXiv:2602.01816*. [https://arxiv.org/abs/2602.01816](https://arxiv.org/abs/2602.01816)

5. Chen, L., et al. (2025). "Illusions in Humans and AI: How Visual Perception Aligns Across Biological and Artificial Systems." *arXiv:2508.12422*. [https://arxiv.org/abs/2508.12422](https://arxiv.org/abs/2508.12422)
