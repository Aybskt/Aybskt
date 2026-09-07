# Profile artwork

The README uses committed animated SVGs. The identity card is based on the existing public profile and Minecraft avatar; the calendar uses real public GitHub contributions.

## Publish

Upload `README.md`, `assets/`, `data/`, `scripts/`, `.github/`, and `.gitignore` to the public `Aybskt/Aybskt` repository. Keep the workflow at `.github/workflows/update-profile.yml`. In Actions, run **Update profile contributions** once. Its daily schedule follows the repository's default branch.

## Maintain

- Refresh calendar: `python scripts/update_profile.py` (Python 3.12+, no dependencies).
- Edit project card copy in `scripts/make_project_cards.py`, then regenerate with `python scripts/make_project_cards.py` (no dependencies).
- Edit technology badges in `scripts/make_toolbox.py`, then regenerate with `python scripts/make_toolbox.py` (no dependencies).
- Edit biography lines in `scripts/make_about.py`, then regenerate with `python scripts/make_about.py` (no dependencies). The typing sequence repeats every 20 seconds with a long reading pause.
- Project demos replay real local CLI runs captured in `data/demo-transcripts.json`, with source commit IDs. Generate SVGs with `python scripts/make_demos.py`. The Java launcher is omitted for readability; these are animated transcripts, not GUI recordings.
- To re-record: clone both project repositories, then run `python scripts/record_demos.py path/to/Metadata-Extractor path/to/Checker-Beautifier-in-Java-for-python-language`. Requires a JDK with `java` and `javac`; uses the metadata repository's bundled JAR for its existing dependencies. Generated fixtures and classes stay under `.git/demo-run/`.
- Scroll-triggered playback exists only in the local web preview. GitHub strips scripts, so README animations cannot detect the page viewport and replay independently instead.
- Test parser: `python -m unittest discover -s scripts -p 'test_*.py'`.
- Regenerate the original-photo panel with `python scripts/make_avatar_scene.py path/to/avatar.png` (no dependencies). The PNG is embedded unchanged inside the SVG; only the frame and scan overlay animate.
- Intro text and contribution reveal run once. The photo scan, terminal signals and cybersecurity lab loop continuously. All animations respect reduced motion; profile details remain available as plain text.
- If GitHub changes its public calendar markup, generation fails and preserves the previous files. Check Actions failures; scheduled workflows may be disabled by GitHub after extended repository inactivity.

Visual direction inspired by [Avi Vashishta's animated profile guide](https://www.avivashishta.com/blog/build-animated-github-profile-readme.html). Artwork and scripts were created for Aybskt.
