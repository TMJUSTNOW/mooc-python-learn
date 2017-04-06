#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysql.TimeCount import TimeCount;
from mysql._mongo_db_ import *

from migration.mysql._mysql_db_ import *

tk = TimeCount();


# 查询所有的小题
def queryPapersQuestions():
    conn, cur = conn_db()
    cur = exe_query(cur, "select id, courseid from score_papers_questions")
    return cur


# 根据小题ID和科目ID查询学生成绩信息
def queryScoreMark(questionsId, courseId):
    conn, cur = conn_db()
    cur = exe_query(cur, "select * from score_mark where questionid = %d and courseid = %d" % (questionsId, courseId))
    return cur


def insertScoreMark(data):
    db = mongodb_conn()
    db.exam_mark.insert(data)


def parseMarkData():
    tk.start()
    questions_cur = queryPapersQuestions();
    for item in questions_cur:
        markDataLit = []
        mark_cur = queryScoreMark(item['id'], item['courseid'])
        for markData in mark_cur:
            # print(markData)
            if markData is None:
                continue
            else:
                doc = {
                    'student_id': markData['studentid'],
                    'question_id': markData['questionid'],
                    'exam_course_id': markData['courseid'],
                    'exam_id': markData['examid']
                    # 'score': data['mark']
                }
                markDataLit.append(doc)
                # break
        if len(markDataLit)  > 0:
            tk.start()
            insertScoreMark(markDataLit)
            tk.stop()
            print(tk)
    tk.stop()
    print(tk)


def main():
    parseMarkData()
    # docList = parseMarkData()
    # insertScoreMark(docList)
    # print(tk)
