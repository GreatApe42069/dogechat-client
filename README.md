
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/7afe4707-c27c-4e30-8cb0-d86b5571f623" />

# 🐶 Đogechat Python client

A `Python` implementation of the Dogechat Đecentralized, peer-to-peer, encrypted, interopable, chat application over BLE.

*This project is a rewrite of the [original Rust-based `bitchat-terminal`](https://github.com/ShilohEye/bitchat-terminal).*

---

## Table of contents

* [Overview](#overview)
* [Installation](#installation)

  * [Prerequisites](#prerequisites)
  * [Clone & Setup (recommended)](#clone--setup)
  * [Install dependencies (pip)](#install-dependencies-pip)

* [Usage](#usage)

  * [Simple start](#simple-start)
  * [CLI startup options](#cli-startup-options)
  * [Dogechat Commands](#dogechat-commands)
  * [Troubleshooting](#troubleshooting)
  * [License](#license)
  * [Contributing](#contributing)
  * [Donations](#donations)

---

## Overview

Đogechat is a peer-to-peer encrypted chat client that uses Bluetooth Low Energy (BLE) to exchange messages with mobile devices and other peers. This Python client is interopable and compatible with the Đogechat Android App in `https://github.com/GreatApe42069/dogechat-android` 

*See bottom of `ReadMe.md` for cross-device interoperability refs*

---

## Installation

### Prerequisites

* **Python**: 3.8+ (3.10+ recommended). Ensure `python` on your PATH points to the interpreter you intend to use.
* **pip**: latest (run `python -m pip install --upgrade pip setuptools wheel`).
* On **Windows**, use a normal CPython distribution (not the MS Store version) for better BLE support.

### Clone & Setup

```bash
# clone repo
git clone https://github.com/GreatApe42069/dogechat-client.git
cd dogechat-client
```

Virtual environments are optional; you can install dependencies directly with your system Python.

### Install dependencies (pip)

A `requirements.txt` is included in the repo.......***Install it***:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

**Minimal dependencies used by this client:**

* `bleak==0.22.3` — BLE library for cross-platform Bluetooth support
* `aioconsole` — interactive asyncio console utilities
* `pybloom-live` — bloom filter utilities
* `cryptography` — encryption primitives used by the client
* `lz4` — compression used for payloads

If you ever hit `ModuleNotFoundError: No module named 'xxx'`, run:

```bash
python -m pip install xxx
```

---

## Usage

### Simple start

With the virtualenv activated:

```bash
python dogechat.py
```

> On Windows make sure the Python you run is the same one you used to install packages (`python -m pip show bleak`) and that your BLE adapter is enabled.

### CLI startup options

The client supports several command-line options and interactive flags. (If your `dogechat.py` prints a `--help` output, that is the canonical reference.) Example:

```bash
python dogechat.py --help
```

### Dogechat Commands

Inside the client you can use the following commands:

```
**General Commands**

* /help               : Show this help menu
* /h                  : Alias for /help
* /me                 : Get your Nickname and peer_id
* /name <name>        : Change your nickname
* /status             : Show connection info
* /clear              : Clear the screen
* /exit               : Quit Dogechat
* /q                  : Alias for /exit

**Navigation Commands**

* 1-9                 : Quick switch to conversation
* /list               : Show all conversations
* /switch             : Interactive conversation switcher
* /public             : Go to public chat

**Messaging Commands**

(Type normally to send in current mode)

* /dm <name>          : Start private conversation
* /dm <name> <msg>    : Send quick private message
* /reply              : Reply to last private message

**Channel Commands**

* /j #channel               : Join or create a channel
* /j #channel <password>    : Join with password
* /leave                    : Leave current channel
* /pass <pwd>               : Set channel password (owner only)
* /transfer @user           : Transfer ownership (owner only)

**Discovery Commands**

* /channels                 : List all discovered channels
* /online                   : Show who's online
* /w                        : Alias for /online

**Privacy & Security Commands**

* /block @user       : Block a user
* /block             : List blocked users
* /unblock @user     : Unblock a user
```

---

## Troubleshooting

**Common: `ModuleNotFoundError`**

* Fix by installing the missing package into the same interpreter:

```bash
python -m pip install <package-name>
```

**Common: Python/pip mismatch**

* Always use `python -m pip` instead of `pip` to ensure the pip installs into the interpreter you expect.

```bash
python -c "import sys; print(sys.executable, sys.version)"
python -m pip show bleak
```

**Windows PowerShell activation error**

* If activation is blocked, temporary allow scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

**BLE not working or runtime BLE errors**

* On Windows, Bleak uses WinRT. Use a non-store CPython and ensure Bluetooth is enabled and accessible to your user account.
* On Linux, ensure BlueZ and appropriate permissions are set (e.g. run with appropriate capabilities or via `sudo` during testing).


---

## License

This project is released into the public domain. See the [LICENSE](LICENSE.md) file for details.

---

## 🛠 Contributing

If you'd like to contribute or donate to this project, please donate in Dogecoin. For active contributors its as easy as opening issues, and or creating pull requests.

This software is Open-source, Đecentralized, an FREE to use, Đonations are accepted, but never expected, to support The Contributers of Đogechat you can send any Donations in Dogecoin, Doginals, Dunes, or Drc-20's to the following Contributors:

***You can donate to*** **GreatApe** ***here:***

"𝕏 handle": ***"GreatApe42069"*** "at": [***"@Greatape42069E"***](https://x.com/Greatape42069E)

 **"Đogecoin_address":** **D9pqzxiiUke5eodEzMmxZAxpFcbvwuM4Hg**


### ***Contributions are welcome! Key areas for enhancement:***

1. **Performance**: Battery optimization and connection reliability
2. **UI/UX**: Additional Material Design features
3. **Security**: Enhanced cryptographic features
4. **Testing**: Unit and integration test coverage
5. **Documentation**: API documentation and development guides

### Support & Issues

- **Bug Reports**: [Create an issue](../../issues) with device info and logs
- **Feature Requests**: [Start a discussion](https://github.com/orgs/greatape42069/discussions)
- **Security Issues**: Email security concerns privately
- **Android Compatibility**:
Cross-reference with [original dogechat Android repo](https://github.com/GreatApe42069/dogechat-android)

Cross-reference with [original bitchat Android repo](https://github.com/permissionlesstech/bitchat-android)

For Android-specific issues, please refer to the [original bitchat-android repository](https://github.com/permissionlesstech/bitchat-android).

- **iOS Compatibility**:
Cross-reference with [original dogechat Android repo](https://github.com/GreatApe42069/dogechat)

Cross-reference with [original iOS repo](https://github.com/jackjackdoges/bitchat)

For iOS-specific issues, please refer to the [original iOS bitchat repository](https://github.com/jackjackdoges/bitchat).


![image](https://github.com/user-attachments/assets/92ad2d4c-b3b1-4464-b9c0-708038634770)


---
