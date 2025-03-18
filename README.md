# GBA ROM Renamer and Organizer  

A simple and easy to use(?) Python script to clean up and organize ROM files. It renames files, removes duplicates, and generates a log to keep track of every change. Supports a bunch of extensions.
Makes it easy to organize roms from various sources and for box art scraping purposes. 
## What It Does  
- **Renames ROMs**: Strips out useless prefixes, numbers, and tags for cleaner filenames.  
- **Removes Duplicates**: Checks for duplicates using SHA256 hashes and deletes them.  
- **Handles Conflicts**: If two ROMs end up with the same name, it adds a numeric suffix.  
- **Keeps Logs**: Generates a `rename_log.txt` so you know what changed.  

## Supported Extensions  
This script doesn’t discriminate — it handles more than just GBA:  
tested on GBA, GBC, GB, cue, bin, and SNES roms so far but should be able to support: `"cas", "2d", "2hd", "2mg", "32x", "3ds", "7z", "88d", "98d", "a0", "a22", "a26", "a52", "a78", "abs", "ace", 
"adf", "adl", "adz", "apk", "arc", "ark", "asc", "asm", "atr", "atr.gz", "atx", "b0", "bas", "bin", "bkd", "c", "c64", "car", "cart", "cas", "cbn", "ccc", "ccd", "cdi", "cdt", "chd", 
"ciso", "cmd", "cod", "cof", "col", "com", "cpc", "cpio", "cpr", "crt", "cso", "csw", "ctg", "ctr", "cue", "d64", "d71", "d77", "d81", "d88", "d98", "dcm", "ddp", "dim", "dmk", "dmp", 
"dms", "do", "doc", "dsd", "dsk", "dup", "dx1", "elf", "exe", "fd", "fdd", "fdi", "fds", "fig", "fpk", "g", "g64", "gam", "game", "gb", "gba", "gbc", "gcz", "gdi", "gen", "gg", "gsplus", 
"gz", "hdd", "hdf", "hdi", "hdm", "hdn", "hdv", "hdz", "hex", "id", "img", "ini", "int", "ipf", "iso", "j64", "jag", "jfd", "jvc", "k7", "lbr", "ldf", "lha", "lnx", "lua", "lutro", "m3u", 
"m5", "m7", "md", "mdf", "mgd", "mgt", "mgw", "min", "msa", "mus", "mx1", "mx2", "n64", "nbz", "ndd", "nds", "nes", "ngc", "ngp", "nhd", "nib", "nrg", "nx", "os9", "p", "p00", "p8", "pak", 
"pbp", "pc2", "pce", "pdb", "pig", "png", "po", "pqa", "prc", "prg", "qd", "rar", "raw", "reu", "rkm", "rom", "rzx", "sad", "sap", "scl", "sda", "sdd", "sfc", "sfx", "sg", "sgx", "singe", 
"slt", "smc", "smd", "sms", "sna", "solarus", "sp", "ssd", "st", "stx", "sub", "sv", "svm", "swc", "szx", "t64", "t77", "tap", "tar", "td0", "tfd", "thd", "tic", "toc", "trd", "tzx", "uae", 
"udi", "uef", "unf", "uze", "v64", "vb", "vboy", "vdk", "vec", "vpk", "vx", "wad", "wasm", "wav", "wbfs", "ws", "wsc", "xdf", "xex", "xfd", "xfd.gz", "xpm", "xz", "z3", "z6", "z64", "z80", "zip", "znx"

## How to Use It  
1. **Install Python** if you don’t have it.  
2. **Run the script**:  
Replace folder_path = r"G:\\garlic\\ROMS" G:\\garlic\\ROMS bing your ROM folder
rename_roms(folder_path)

python uniromOrganizer.py
