# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("HELP 📜", callback_data="helpcallback"),
                InlineKeyboardButton("ABOUT ⁉️", callback_data="aboutcallback")
            ]
        ])
    
    CHOOSE_E_F__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("FILE EXTRACT 📂", callback_data="extract_file|tg_file|no_pass"),
            ],
            [
                InlineKeyboardButton("FILE (PASSWORD) EXTRACT 📂", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("CANCEL ❌", callback_data="cancel_dis")
            ]
        ])

    CHOOSE_E_U__BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔗 URL EXTRACT 📂", callback_data="extract_file|url|no_pass"),
            ],
            [
                InlineKeyboardButton("🔗 (PASSWORD) URL EXTRACT 📂", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("CANCEL ❌", callback_data="cancel_dis")
            ]
        ])

    CLN_BTNS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("CLEAN MY FILES 😇", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! NOOO 😳", callback_data="nobully")
            ]
        ])
    
    ME_GOIN_HOME = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("BACK 🏡", callback_data="megoinhome")
            ]
        ])

    SET_UPLOAD_MODE_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("UPLOAD AS FILE 📁", callback_data="set_mode|doc")
            ],
            [
                InlineKeyboardButton("UPLOAD AS VIDEO 📹", callback_data="set_mode|video")
            ]
        ])


class Messages:
    START_TEXT = """
Hi **{}**, I'm An **Extract Files Bot** 😇!

Send Your Archive File, Select The Appropriate Options You Wish To. You Can Clear Your All Files With `/clean` Your Process Queue Will Be Cleared. If Anything Is Uploading At Now, It Will Be Cleared. Be Careful ⚠️.

🍒 Supported Formats: **7Z, APM, ARJ, BZ2, BZIP2, CAB, CHM, CPIO, CRAMFS, DEB, DMG, FAT, GZ, GZIP, HFS, ISO, LZH, LZMA, LZMA2, MBR, MSI, MSLZ, NSIS, NTFS, RAR, RPM, SQUASHFS, TAR, TAR.BZ2, TAR.GZ, TAR.XZ, TBZ2, TGZ, UDF, VHD, WIM, XAR, Z, ZIP**

**Powered By @Modzilla**
    """

    HELP_TXT = """
**How To Extract? 🤔**

`1. Send The File Or Link That You Want To Extract.`
`2. Click On Extract Button (If you sent a link use "Url Extract" button. If it's a file just use "File Extract" button).`


**Note:**
    **1.** `If your archive is password protected select` **(Password) Extract 📂** `mode. Bot isn't a GOD to know your file's password so If this happens just send that password!`
    
    **2.** `Please don't send corrupted files! If you sent a one by a mistake just send` **/clean** `command!`
    
    **3.** `If your archive have 95 or more files in it then bot can't show all of extracted files to select from. So in that case if you can't see your file in the buttons just click on` "Upload All ♻️" `button. It'll send all extracted files to you!`
    """

    ABOUT_TXT = """
**About Extract Files Bot,**

✘ **Language:** [Python](https://www.python.org/)
✘ **Framework:** [Pyrogram](https://docs.pyrogram.org/)
✘ **Source Code:** [Itz-fork/Unzipper-Bot](https://t.me/NOSOURCECODE)
✘ **Developer:** [Modzilla](https://t.me/Iggie)


**Made with ❤️ by @Modzilla**
    """

    LOG_TXT = """
**Extract Log 📝!**

**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**Successfully Downloaded**

**Download time:** `{}`
**Status:** `Trying to extract the archive`
    """

    EXT_OK_TXT = """
**Extraction Successfull!**

**Extraction time:** `{}`
**Status:** `Trying to upload`
    """

    EXT_FAILED_TXT = """
**Extraction Failed 😕!**

**What to do?**

 - `Please make sure archive isn't corrupted`
 - `Please make sure that you selected the right mode!`
 - `May be Your archive format isn't supported 😔`

**Please report this at @Iggie if you think this is a serious error**
    """

    ERROR_TXT = """
**Error Happend 😕!**

**ERROR:** {}


**Please report this at @Nexa_bots if you think this is a serious error**
    """

    CANCELLED_TXT = """
**{} ✅!**

`Now all of your files have been deleted from my server 😏!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server 🤔?**

**Note:** `This action cannot be undone!`
    """

SELECT_UPLOAD_MODE_TXT = """
`Please select the upload mode by clicking on below buttons!`
**Current Upload Mode Is:** `{}`
"""
    CHANGED_UPLOAD_MODE_TXT = """
**Successfully Changed Upload Mode To** `{}` **✅!**
"""


# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]
