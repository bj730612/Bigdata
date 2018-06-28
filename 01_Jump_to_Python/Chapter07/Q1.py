from xml.etree.ElementTree import Element, SubElement, dump

blog = Element("blog")
blog.attrib["date"] = "20151231"

subject = Element("subject")
subject.text = "Why python?"
blog.append(subject)
SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is too short, You need Python!"

def indent(elem, level = 0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(blog)
dump(blog)
