<p>
  <a href="https://learnsome.tech/courses/testing-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Automated Testing, TDD & Quality Engineering

**Test Pyramids, Boundary Mocking, Playwright & CI Gates**

5 modules, 24 lessons: What A Test Is For; Unit Testing In Practice; Test Doubles And Boundaries; Testing Time, Files And Services; Quality Gates And Code Review. Beginner level, about 1 hour.

This repository holds the labs of the LearnSome.tech course [Automated Testing, TDD & Quality Engineering](https://learnsome.tech/courses/testing-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/testing-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/testing-labs.git
  cd testing-labs
  ./check m01l01-03
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-03`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Graded | Runs the program and compares its output with `expected.txt`. | 49 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 31 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: What A Test Is For

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [The Cost And Value Of A Test](https://learnsome.tech/learn/testing-course/m01l01) | [4 labs](labs/m01l01/) | Free |
| 1.2 | [Arrange, Act, Assert](https://learnsome.tech/learn/testing-course/m01l02) | [5 labs](labs/m01l02/) | Free |
| 1.3 | [One Assertion Per Reason](https://learnsome.tech/learn/testing-course/m01l03) | [5 labs](labs/m01l03/) | Free |
| 1.4 | [The Test Pyramid And Where It Is Wrong](https://learnsome.tech/learn/testing-course/m01l04) | [4 labs](labs/m01l04/) | Free |
| 1.5 | [Coverage: Diagnostic, Not Target](https://learnsome.tech/learn/testing-course/m01l05) | [4 labs](labs/m01l05/) | Pro |

### Module 2: Unit Testing In Practice

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Introducing pytest](https://learnsome.tech/learn/testing-course/m02l01) | [4 labs](labs/m02l01/) | Pro |
| 2.2 | [Parametrised Tests](https://learnsome.tech/learn/testing-course/m02l02) | [5 labs](labs/m02l02/) | Pro |
| 2.3 | [Fixtures And Their Scope](https://learnsome.tech/learn/testing-course/m02l03) | [5 labs](labs/m02l03/) | Pro |
| 2.4 | [Naming Tests For Readability](https://learnsome.tech/learn/testing-course/m02l04) | [5 labs](labs/m02l04/) | Pro |
| 2.5 | [Making Failures Explain Themselves](https://learnsome.tech/learn/testing-course/m02l05) | [6 labs](labs/m02l05/) | Pro |

### Module 3: Test Doubles And Boundaries

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [What Test Doubles Are For](https://learnsome.tech/learn/testing-course/m03l01) | [5 labs](labs/m03l01/) | Pro |
| 3.2 | [Fakes, Stubs, Mocks And Spies](https://learnsome.tech/learn/testing-course/m03l02) | [5 labs](labs/m03l02/) | Pro |
| 3.3 | [Why Over-Mocking Breeds False Positives](https://learnsome.tech/learn/testing-course/m03l03) | [5 labs](labs/m03l03/) | Pro |
| 3.4 | [Testing Time And Randomness](https://learnsome.tech/learn/testing-course/m03l04) | [4 labs](labs/m03l04/) | Pro |
| 3.5 | [Testing The Filesystem](https://learnsome.tech/learn/testing-course/m03l05) | [4 labs](labs/m03l05/) | Pro |

### Module 4: Testing Time, Files And Services

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [Flaky Tests And How To Kill Them](https://learnsome.tech/learn/testing-course/m04l01) | [3 labs](labs/m04l01/) | Pro |
| 4.2 | [Integration Testing With Containers](https://learnsome.tech/learn/testing-course/m04l02) | [1 lab](labs/m04l02/) | Pro |
| 4.3 | [Contract Testing Between Services](https://learnsome.tech/learn/testing-course/m04l03) | [1 lab](labs/m04l03/) | Pro |
| 4.4 | [Load Testing: Percentiles Over Means](https://learnsome.tech/learn/testing-course/m04l04) | – | Pro |
| 4.5 | [Testing With Real Databases](https://learnsome.tech/learn/testing-course/m04l05) | [1 lab](labs/m04l05/) | Pro |

### Module 5: Quality Gates And Code Review

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Code Review As A Quality Gate](https://learnsome.tech/learn/testing-course/m05l01) | [1 lab](labs/m05l01/) | Pro |
| 5.2 | [What To Look For In A Review](https://learnsome.tech/learn/testing-course/m05l02) | [1 lab](labs/m05l02/) | Pro |
| 5.3 | [What To Automate Away](https://learnsome.tech/learn/testing-course/m05l03) | [1 lab](labs/m05l03/) | Pro |
| 5.4 | [Writing Actionable Review Comments](https://learnsome.tech/learn/testing-course/m05l04) | [1 lab](labs/m05l04/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
