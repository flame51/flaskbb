# -*- coding: utf-8 -*-
"""
    flaskbb.utils.search
    ~~~~~~~~~~~~~~~~~~~~

    This module contains all the whoosheers for FlaskBB's
    full text search.

    :copyright: (c) 2016 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import whoosh
from flask_whooshee import AbstractWhoosheer

from flaskbb.forum.models import Forum, Topic, Post
from flaskbb.user.models import User


class PostWhoosheer(AbstractWhoosheer):
    models = [Post]

    schema = whoosh.fields.Schema(
        post_id=whoosh.fields.NUMERIC(stored=True, unique=True),
        username=whoosh.fields.TEXT(),
        modified_by=whoosh.fields.TEXT(),
        content=whoosh.fields.TEXT()
    )

    @classmethod
    def update_post(cls, writer, post):
        writer.update_document(
            post_id=post.id,
            username=post.username,
            modified_by=post.modified_by,
            content=post.content
        )

    @classmethod
    def insert_post(cls, writer, post):
        writer.add_document(
            post_id=post.id,
            username=post.username,
            modified_by=post.modified_by,
            content=post.content
        )

    @classmethod
    def delete_post(cls, writer, post):
        writer.delete_by_term('post_id', post.id)


class TopicWhoosheer(AbstractWhoosheer):
    models = [Topic]

    schema = whoosh.fields.Schema(
        topic_id=whoosh.fields.NUMERIC(stored=True, unique=True),
    )

    @classmethod
    def update_topic(cls, writer, topic):
        writer.update_document(
            topic_id=topic.id,
        )

    @classmethod
    def insert_topic(cls, writer, topic):
        writer.add_document(
            topic_id=topic.id,
        )

    @classmethod
    def delete_topic(cls, writer, topic):
        writer.delete_by_term('topic_id', topic.id)


class ForumWhoosheer(AbstractWhoosheer):
    models = [Forum]

    schema = whoosh.fields.Schema(
        forum_id=whoosh.fields.NUMERIC(stored=True, unique=True),
    )

    @classmethod
    def update_forum(cls, writer, forum):
        writer.update_document(
            forum_id=forum.id,
        )

    @classmethod
    def insert_forum(cls, writer, forum):
        writer.add_document(
            forum_id=forum.id,
        )

    @classmethod
    def delete_forum(cls, writer, forum):
        writer.delete_by_term('forum_id', forum.id)


class UserWhoosheer(AbstractWhoosheer):
    models = [User]

    schema = whoosh.fields.Schema(
        user_id=whoosh.fields.NUMERIC(stored=True, unique=True),
    )

    @classmethod
    def update_user(cls, writer, user):
        writer.update_document(
            user_id=user.id,
        )

    @classmethod
    def insert_user(cls, writer, user):
        writer.add_document(
            user_id=user.id,
        )

    @classmethod
    def delete_user(cls, writer, user):
        writer.delete_by_term('user_id', user.id)
