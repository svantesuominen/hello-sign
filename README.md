# HelloSign Bulk Document Downloader

## Overview
This Python script was generated to save time and effort by automating the download of more than 100 signed documents from HelloSign, rather than manually downloading each one by hand. It uses the HelloSign API to fetch and download documents in batches, automatically managing the platform's rate limits to avoid errors.

## Features
- **Bulk Download**: Downloads all documents associated with your HelloSign account.
- **File Naming**: Names each file using the document's title for easy identification.
- **Rate Limit Management**: Handles rate limits by pausing after every 20 downloads and providing a dynamic countdown in the terminal.
- **Easy Setup**: Requires only your HelloSign API key to start downloading.

## Why?
This was generated to spare my trackpad finger from downloading more than 100 signed documents one by one.

## How?
1. Create an API key: https://app.hellosign.com/home/myAccount?current_tab=api
2. Plase the API key to the file, run, and enjoy the ride. 
