import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))