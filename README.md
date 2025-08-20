<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/7afe4707-c27c-4e30-8cb0-d86b5571f623" />

# 🐶 Đogechat Python client

A `Python` implementation of the Dogechat Đecentralized, peer-to-peer, encrypted chat application over BLE.

*This project is a rewrite of the [original Rust-based `bitchat-terminal`](https://github.com/ShilohEye/bitchat-terminal).*

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
  * [Simple start](#simple-start)
  * [CLI startup options](#cli-startup-args)
  * [Dogechat Commands](#dogechat-commands)
* [Clone, Develop and Build](#clone-develop-and-build)
  * [Setup environment](#clone-and-setup-editable-environment-using-uv)
  * [Build](#build-sdist-and-wheel)



## Usage

### Simple start
```Shell
python3 dogechat.py
```



### Dogechat Commands

This section details the various commands available within Dogechat.
```shell
General Commands

* `/help`               : Show this help menu
* `/h`                  : Alias for /help
* `/me`                 : Get your Nickname and peer_id
* `/name <name>`        : Change your nickname
* `/status`             : Show connection info
* `/clear`              : Clear the screen
* `/exit`               : Quit Dogechat
*  `/q`                 : Alias for /exit


Navigation Commands

* `1-9`                 : Quick switch to conversation
* `/list`               : Show all conversations
* `/switch`             : Interactive conversation switcher
* `/public`             : Go to public chat


Messaging Commands

(Type normally to send in current mode)

* `/dm <name>`          : Start private conversation
* `/dm <name> <msg>`    : Send quick private message
* `/reply`              : Reply to last private message


Channel Commands

* `/j #channel`               : Join or create a channel
* `/j #channel <password>`    : Join with password
* `/leave`                    : Leave current channel
* `/pass <pwd>`               : Set channel password (owner only)
* `/transfer @user`           : Transfer ownership (owner only)


Discovery Commands

* `/channels`                 : List all discovered channels
* `/online`                   : Show who`s online
* `/w`                        : Alias for /online


Privacy & Security Commands

* `/block @user`       : Block a user
* `/block`             : List blocked users
* `/unblock @user`     : Unblock a user
```

## License

This project is released into the public domain. See the [LICENSE](LICENSE.md) file for details.


## 🛠 Contributing

If you'd like to contribute or donate to this project, please donate in Dogecoin. For active contributors its as easy as opening issues, and or creating pull requests.

This software is Open-source, Đecentralized, an FREE to use, Đonations are accepted, but never expected, to support The Contributers of Đogechat you can send any Donations in Dogecoin, Doginals, Dunes, or Drc-20's to the following Contributors:

***You can donate to*** **GreatApe** ***here:***

"handle": ***"GreatApe42069"*** "at": [***"@Greatape42069E"***](https://x.com/Greatape42069E)

 **"Đogecoin_address":** **D9pqzxiiUke5eodEzMmxZAxpFcbvwuM4Hg**


## ***Contributions are welcome! Key areas for enhancement:***

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


