
import os
import re
import hashlib

# Supported extensions
SUPPORTED_EXTENSIONS = {"cas", "2d", "2hd", "2mg", "32x", "3ds", "7z", "88d", "98d", "a0", "a22", "a26", "a52", "a78", "abs", "ace", "adf", "adl", "adz", "apk", "arc", "ark", "asc", "asm", "atr", "atr.gz", "atx", "b0", "bas", "bin", "bkd", "c", "c64", "car", "cart", "cas", "cbn", "ccc", "ccd", "cdi", "cdt", "chd", "ciso", "cmd", "cod", "cof", "col", "com", "cpc", "cpio", "cpr", "crt", "cso", "csw", "ctg", "ctr", "cue", "d64", "d71", "d77", "d81", "d88", "d98", "dcm", "ddp", "dim", "dmk", "dmp", "dms", "do", "doc", "dsd", "dsk", "dup", "dx1", "elf", "exe", "fd", "fdd", "fdi", "fds", "fig", "fpk", "g", "g64", "gam", "game", "gb", "gba", "gbc", "gcz", "gdi", "gen", "gg", "gsplus", "gz", "hdd", "hdf", "hdi", "hdm", "hdn", "hdv", "hdz", "hex", "id", "img", "ini", "int", "ipf", "iso", "j64", "jag", "jfd", "jvc", "k7", "lbr", "ldf", "lha", "lnx", "lua", "lutro", "m3u", "m5", "m7", "md", "mdf", "mgd", "mgt", "mgw", "min", "msa", "mus", "mx1", "mx2", "n64", "nbz", "ndd", "nds", "nes", "ngc", "ngp", "nhd", "nib", "nrg", "nx", "os9", "p", "p00", "p8", "pak", "pbp", "pc2", "pce", "pdb", "pig", "png", "po", "pqa", "prc", "prg", "qd", "rar", "raw", "reu", "rkm", "rom", "rzx", "sad", "sap", "scl", "sda", "sdd", "sfc", "sfx", "sg", "sgx", "singe", "slt", "smc", "smd", "sms", "sna", "solarus", "sp", "ssd", "st", "stx", "sub", "sv", "svm", "swc", "szx", "t64", "t77", "tap", "tar", "td0", "tfd", "thd", "tic", "toc", "trd", "tzx", "uae", "udi", "uef", "unf", "uze", "v64", "vb", "vboy", "vdk", "vec", "vpk", "vx", "wad", "wasm", "wav", "wbfs", "ws", "wsc", "xdf", "xex", "xfd", "xfd.gz", "xpm", "xz", "z3", "z6", "z64", "z80", "zip", "znx"}

def get_file_hash(filepath):
    """Generate SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def rename_roms(folder_path):
    # Verify the folder exists
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path: {folder_path}")
        return

    # Get all files that match supported extensions
    files = [f for f in os.listdir(folder_path) if f.split('.')[-1].lower() in SUPPORTED_EXTENSIONS]

    # Clean up names: remove numeric prefixes, leading underscores, '- ' prefixes, and sort alphabetically
    cleaned_names = []
    prefix_pattern = re.compile(r'^(\d+_\d+|\d+|_+|-\s*)\s*')
    suffix_pattern = re.compile(r'\s*\((U|UE|UA|M\d+)\)\s*')
    
    for file in files:
        cleaned_name = prefix_pattern.sub('', file)
        cleaned_name = suffix_pattern.sub('', cleaned_name)
        cleaned_names.append((file, cleaned_name))

    # Sort files based on cleaned names (case-insensitive)
    cleaned_names.sort(key=lambda x: x[1].lower())

    # Track seen names and hashes to detect duplicates and handle conflicts
    seen_names = {}
    seen_hashes = {}

    # Rename files and create a log
    log_path = os.path.join(folder_path, 'rename_log.txt')
    with open(log_path, 'w', encoding='utf-8') as log_file:
        for original, cleaned in cleaned_names:
            old_path = os.path.join(folder_path, original)
            file_hash = get_file_hash(old_path)

            # Nuke duplicates immediately
            if file_hash in seen_hashes:
                os.remove(old_path)
                log_file.write(f"{original} -> Deleted (duplicate of {seen_hashes[file_hash]})\n")
                continue

            # Handle name conflicts by numbering sequentially
            base_name, ext = os.path.splitext(cleaned)
            count = seen_names.get(base_name, 0) + 1
            seen_names[base_name] = count
            new_name = f"{base_name} ({count:03}){ext}" if count > 1 else cleaned

            seen_hashes[file_hash] = new_name
            new_path = os.path.join(folder_path, new_name)

            # Skip renaming if old and new paths are the same
            if old_path != new_path:
                # Remove the conflicting file if it exists
                if os.path.exists(new_path):
                    os.remove(new_path)

                os.rename(old_path, new_path)
                log_file.write(f"{original} -> {new_name}\n")
            else:
                log_file.write(f"{original} -> (unchanged)\n")

    print(f"Renaming complete. Log saved to {log_path}")

if __name__ == "__main__":
    folder_path = r"G:\\garlic\\ROMS"
    rename_roms(folder_path)
