import markdown, codecs

input_file = codecs.open("provisioning_notes.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

output_file = codecs.open("provisioning_notes.html", "w", encoding="utf-8", errors="xmlcharrefreplace")
output_file.write(html)