# AI-use disclosure templates

From 白皮书 ch.7 §披露与诚信. Place in the paper. Adapt to what the student ACTUALLY did — never
misrepresent. Disclosure is REQUIRED by the official 2026 rules
(https://www.yau-awards.com/show-86-59.html, verified 2026-08-27): the Acknowledgements page
must state each use's 工具名称 / 版本 / 使用环节 / 使用频率, and the matching chat logs must be
retained for submission. These templates organize exactly those four elements.

## Acknowledgements (blanket, for non-core assistance)
```
We acknowledge the use of ChatGPT (GPT-4, OpenAI) and Claude (Anthropic) for language polishing
and code-level debugging assistance throughout this project. All algorithmic design, experimental
decisions, data analysis, and core conclusions reported in this paper are the work of the authors.
Generative AI was not used to formulate research questions, generate data, or derive theoretical
results.
```
Adjust the last sentence to match reality. If AI WAS part of the method, that belongs in Methods
(below), not denied here.

## Methods (specific, when AI is a substantive method component)
```
For semantic classification, we fine-tuned the BERT-base-uncased model (Devlin et al., 2019) on
a custom dataset of 4,217 manually annotated samples. Training used the AdamW optimizer (learning
rate 2e-5, batch size 16) for 5 epochs on an NVIDIA A100 GPU. Model performance was evaluated
using five-fold cross-validation with macro-F1 as the primary metric.
```
Always cite the original model/dataset/algorithm paper. Report version, hyperparameters,
evaluation — these are exactly what judges probe.

## Answering "did you use AI?" at defense (layered disclosure)
Framework (ch.7 §答辩如何回应):
> "Yes, for {X} I used {tool} to {specific task}, mainly because {reason}. However, {core insight
> / decision} was mine, reached through {specific reasoning}; AI was not decisive there. I can
> derive/demonstrate that part now if you'd like."

Avoid both extremes: panicked denial (detectable, fatal) and over-confession (makes it sound like
AI did most of the work). Steer the conversation to the detail you own best.

## What NOT to do (ch.7 §常见误区)
- Don't call trivial AI polishing "no AI use" — small lies, once caught, sink overall credibility.
- Don't paste AI-generated citations.
- Don't put AI-derived statistics in the paper without local reproduction (keep an executable
  notebook).
