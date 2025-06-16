# Changelog – GPT OS

All notable changes to this project will be documented in this file.

## [v0.1] – 2025-06-12
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

## [v0.2] – 2025-06-14
### Added
- Command replay system (`replay <index>`, `replay last`)
- Persistent command logging (`log save`, `log load`)
- Modular `log_plugin` for log control
- `.gptos/` hidden folder for internal state
- Bug fixes related to command logging and singleton logger instance

## [v0.3] – 2025-06-16
### Added
- Ethics integration finalized with strict mode support


## [v0.4] - 2025-06-16
### Changes
- Alias system enhanced with multi-token resolution and persistent storage
- Memory plugin refactored with indexing and deduplication features
- Summarizer plugin added for recent command summaries
- Command logging improved with search, replay, and filters
- Setup.cfg and release script updates for versioning and changelog automation

