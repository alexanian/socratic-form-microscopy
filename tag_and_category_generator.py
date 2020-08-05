#!/usr/bin/env python

'''
based on tag_generator by Long Qian (https://longqian.me/2017/02/09/github-jekyll-tag/)

'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'
categories_dir = 'category/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
total_categories = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    in_tags_section = False
    in_categories_section = False
    for line in f:
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                in_tags_section = False
                in_categories_section = False
                break
        elif crawl:
            if line.strip() == 'tags:':
                in_tags_section = True
                in_categories_section = False
            elif line.strip() == 'categories:':
                in_tags_section = False
                in_categories_section = True
            elif in_tags_section:
                tag_name = line.strip().replace("- ", '').replace('"', "'")
                tag_slug = tag_name.replace("'", '').replace(' ', '-')
                print("Tag: " + tag_name)
                total_tags.extend([tag_name + '|' + tag_slug])
            elif in_categories_section:
                category_name = line.strip().replace("- ", '').replace('"', "'")
                category_slug = category_name.replace("'", '').replace(' ', '-').lower()
                print("Category: " + category_name)
                total_categories.extend([category_name + '|' + category_slug])
    f.close()
total_tags = set(total_tags)
total_categories = set(total_categories)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

old_categories = glob.glob(categories_dir + '*.md')
for category in old_categories:
    os.remove(category)
    
if not os.path.exists(categories_dir):
    os.makedirs(categories_dir)

print()
for tag in total_tags:
    tag_name, tag_slug = tag.split('|')
    tag_filename = tag_dir + tag_slug + '.md'
    print("Creating " + tag_filename)
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag_name + '\"\ntag: ' + tag_name + '\n---\n'
    f.write(write_str)
    f.close()

print()

for category in total_categories:
    category_name, category_slug = category.split('|')
    category_filename = categories_dir + category_slug + '.md'
    print("Creating " + category_filename)
    f = open(category_filename, 'a')
    write_str = '---\nlayout: categorypage\ntitle: \"Category: ' + category_name + '\"\ncategory: ' + category_name + '\n---\n'
    f.write(write_str)
    f.close()

print()
print("Tags generated: ", total_tags.__len__())
print("Categories generated: ", total_categories.__len__())
