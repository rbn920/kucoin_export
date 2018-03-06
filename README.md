# kucoin_export
Exports Kucoin trade and deposit/withdrawal history to JSON and CSV. Forwhatever reason Kucoin does not offer a way to export your
history so I hacked this together from a few other things I have been working on.
## Installation
```pip install kucoin_export```
## Usage
### Add your keys
First you to import your api keys. The keys are encrypted and stored in the config.ini file.

```kucoin add_exchange your_key your_secret_key```

You will be prompted for a password twice. This is not your kucoin password. It is used for encrypting/decrypting your api keys.
### Get you trade history
```kucoin trade_history```

You will be prompted for the password you used when adding your keys. The process of getting the trade history is quite slow. It
will probably take 8 to 10 minutes. This is due to the number of requests that are required to get you full history.
### Get you deposit/withdrawal history
```kucoin transfer_history```

You will be prompted for the password you used when adding your keys. As mentioned above, this will probably take 8 to 10 minutes.
