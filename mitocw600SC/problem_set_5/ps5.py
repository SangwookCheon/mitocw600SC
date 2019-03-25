# 6.00 Problem Set 5
# RSS Feed Filter
# Name: Sangwook Cheon
# Collaborators: None
# Time: 3 hours

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = (str(word).lower()).translate(None, string.punctuation)
        # print self.word
        self.w_list = []

    def is_word_in(self, text):
        for i in string.punctuation:
            text = str(text).lower().replace(i, " ")
        self.w_list = text.split()
        # print self.w_list
        if self.word in self.w_list:
            return True
        else:
            return False

    def evaluate(self, text):
        return WordTrigger.is_word_in(self, text)

# TODO: TitleTrigger


class TitleTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
        self.title = ''

    def evaluate(self, object):
        self.title = object.get_title()
        # print self.title
        return WordTrigger.is_word_in(self, self.title)

# TODO: SubjectTrigger


class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
        self.subject = ''

    def evaluate(self, object):
        self.subject = object.get_subject()
        return WordTrigger.is_word_in(self, self.subject)
# TODO: SummaryTrigger


class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word)
        self.summary = ''

    def evaluate(self, object):
        self.summary = object.get_summary()
        return WordTrigger.is_word_in(self, self.summary)

# o1 = NewsStory('',"soft's, I am.",'','','')
# s1 = TitleTrigger('soft')
# print s1.evaluate(o1)
# Composite Triggers
# Problems 6-8

# TODO: NotTrigger


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, nitem):
        return not self.trigger.evaluate(nitem)
# TODO: AndTrigger


class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, nitem):
        return self.trigger1.evaluate(nitem) and self.trigger2.evaluate(nitem)
# TODO: OrTrigger


class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, nitem):
        return self.trigger1.evaluate(nitem) or self.trigger2.evaluate(nitem)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
        self.tlist = []

    def evaluate(self, nitem):
        self.tlist = []
        self.tlist.extend((nitem.get_title(), nitem.get_subject(), nitem.get_summary()))
        for i in range(len(self.tlist)):
            if self.phrase in self.tlist[i]:
                return True

# ======================
# Part 3
# Filtering
# ======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    storylist = []
    for story in stories:
        for trigger in triggerlist:
            # print '-------________________________________'
            # print type(trigger)
            if trigger.evaluate(story):
                storylist.append(story)
                # print "current story list: " + str(storylist)
            # else:
                # print 'not in'
                # print "the story's title was: " + str(story.get_title())
                # print "the story's subject was: " + str(story.get_subject())

    return storylist

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    llist = []
    names = {}
    triggerset = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    for line in lines:
        llist = line.split()
        if llist[0] != 'ADD':
            names[llist[0]] = ''
            if llist[1] == 'SUBJECT':
                names[llist[0]] = SubjectTrigger(llist[2])
                # print "type of subject: " + str(type(names['t2']))
            elif llist[1] == 'TITLE':
                names[llist[0]] = TitleTrigger(llist[2])
            elif llist[1] == 'SUMMARY':
                names[llist[0]] = SummaryTrigger(llist[2])
            elif llist[1] == 'PHRASE':
                names[llist[0]] = PhraseTrigger(llist[2])
                # print "type of phrase: " + str(type(names['t3']))
            elif llist[1] == 'AND':
                names[llist[0]] = AndTrigger(names[llist[2]], names[llist[3]])
                # print 'trigger 1: ' + str(names['t4'].trigger1), str(type(names['t4'].trigger1))
                # print 'trigger 2: ' + str(names['t4'].trigger2), str(type(names['t4'].trigger2))
            elif llist[1] == 'OR':
                names[llist[0]] = OrTrigger(llist[2], llist[3])
            elif llist[1] == 'NOT':
                names[llist[0]] = NotTrigger(llist[2])
            # print names
        else:
            for item in range(1, len(llist)):
                triggerset.append(names[llist[item]])
                # print "triggerset: " + str(triggerset)
    # a = NewsStory('','Hi, my name is name is NFL','','','')
    # print '---------'
    # print triggerset[0].evaluate(a)

    return triggerset

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    # t1 = SubjectTrigger("Obama")
    # t2 = SummaryTrigger("MIT")
    # t3 = PhraseTrigger("Supreme Court")
    # t4 = OrTrigger(t2, t3)
    # triggerlist = [t1, t4]

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)

        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

