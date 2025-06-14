# Changelog – GPT OS

All notable changes to this project will be documented in this file.

## [0.1.0] – 2025-06-12
### Added
- Command parser and executor (command_core)
- Memory core with summarizer and recorder
- Ethics guard with strict mode support
- Plugin loader with hot-reloading
- Alias manager and config runtime overrides
- Devtools plugin (echo, simulate, debug)
- Philosophy plugin (question, thoughts)
- Help and status plugins
- Architecture and README documentation

## [v0.2] - 2025-06-14
### Added
- Command replay system (`replay <index>`, `replay last`)
- Persistent command logging (`log save`, `log load`)
- Modular `log_plugin` for log control
- `.gptos/` hidden folder for internal state

### Fixed
- Bug where command logging failed due to missing `raw_input`
- Unified `CommandLogger` to singleton instance

## [v0.2] - 2025-06-14
### Changes
db87235 chore: release v0.2
4c7674c chore: finalize GPT OS v0.2 with logging and replay