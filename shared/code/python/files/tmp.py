import tempfile


with tempfile.TemporaryFile(mode="w+", encoding="utf8") as fh:
    fh.write(template.render())
