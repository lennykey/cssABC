#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import re
import os
import sys

def main(css):
    # f = open('test.css', 'r')
    print("innerCSSABC")

    # logging.warning(f.read())
    # logging.warning("Test")

    # text = f.read()
    text = css.encode("utf-8")
    # print(text)
    # kommtentare = re.compile(r"((/\*)+.*?(\*/)+)", re.DOTALL)
    # text = re.sub(kommtentare, "", text)
    groups = re.findall(r".*?{.*?}", text, re.DOTALL)
    # logging.warning(found)

    # f.close()

    sortedGroups = sortCSS(groups) 
    return writeSortedCSSToString(sortedGroups)
    # writeSortedCSSToFile("sortedCSS.css", sortedGroups)
    # logging.warning(sortedCSS)

def writeSortedCSSToString(groups):
    sortedCss = []

    for group in groups:
        for tagname, attributes in group.items():
            # logging.warning(tagname)
            # sepline.warning(value)
            sortedCss.append(os.linesep+tagname+"{"+os.linesep)
            for attribute in attributes:
                    sortedCss.append("    "+str(attribute)+os.linesep)
        sortedCss.append("}")

    # logging.warning(sortedCss)
    return ''.join(sortedCss).decode("utf-8")



def writeSortedCSSToFile(filename, groups):
    f = open(filename, "w")

    for group in groups:
        for tagname, attributes in group.items():
            # logging.warning(tagname)
            # sepline.warning(value)
            f.write(os.linesep+tagname+"{"+os.linesep)
            for attribute in attributes:
                    f.write("    "+str(attribute)+os.linesep)
        f.write("}")

    f.close()

def sortCSS(css):
    sortedCSS = []
    for entry in css:
        response = []
        # innerFound = re.findall(r"{+.*?}+", entry, re.DOTALL)
        # logging.warning(entry)
        # entry = ' '.join(entry.split())
        # logging.warning(entry)
        taglong = re.search(r"(.*{)", entry, re.DOTALL)
        tagname = taglong.group(1).replace("{", "")
        taglong = taglong.group(1)
        # logging.warning(tag)
        # logging.warning(taglong.group(1))
        # myTag = "".join( str(tag).replace(" {", "") )
        # logging.warning(myTag)

        comments = re.findall(r"(/\*.*?\*/)", entry.replace(taglong, ""), re.DOTALL)
        # logging.warning(comments)
        # logging.warn("Comment:" + str(comments))
        commentPattern = re.compile(r"(/\*.*?\*/)", re.DOTALL)
        cleanedEntry = commentPattern.sub("", entry.replace(taglong, ""));
        # logging.warning(cleanedEntry)
        # attributes = [ a.strip() for a in re.findall(r"(?<!/).*?;", entry) ]
        attributes = [ a.strip() for a in re.findall(r"[^ \t]+?:[ \t]*?[^ \t]+?[;|}]", cleanedEntry) ]
        # logging.warning("Attribute: " + str(attributes))
        for attribute in attributes:
            # logging.warn(attribute)
            response.append( re.sub(r"\s", "", attribute.replace(";","").replace("}", "")+";") )
            # print "Group", i, ":", attribute.group(i)
        
        # logging.warning(response)

        for comment in comments:
            # logging.warning(comment.replace("/*", "").replace("*/", "").strip())
            if comment.replace("*/", "").strip() not in attributes:
                response.append(comment)
        # attribute.append(comments)
        # firstAttribute = attribute.group(0)
        # logging.warning(firstAttribute)
        # length = len(attribute.groups())
        # for i in xrange(length + 1):


        cssAttributesSorted = sorted(response)
        # logging.warning(cssAttributesSorted)

        myDict = {tagname:cssAttributesSorted}
        # logging.warning(myDict)

        sortedCSS.append(myDict)

    return sortedCSS

if __name__ == "__main__":
    main(css)