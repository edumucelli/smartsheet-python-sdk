# pylint: disable=C0111,R0902,R0904,R0912,R0913,R0915,E1101
# Smartsheet Python SDK.
#
# Copyright 2017 Smartsheet.com, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import

import six
import json

from .user import User
from .recipient import Recipient
from ..util import serialize
from ..util import deserialize
from ..types import TypedList
from datetime import datetime
from dateutil.parser import parse


class SentUpdateRequest(object):
    """Smartsheet SentUpdateRequest data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the SentUpdateRequest model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj

        self.allowed_values = {
            'update_request_status': [
                'PENDING',
                'COMPLETE',
                'CANCELED']}

        self._column_ids = TypedList(six.integer_types)
        self._id_ = None
        self._include_attachments = None
        self._include_discussions = None
        self._message = None
        self._row_ids = TypedList(six.integer_types)
        self._sent_at = None
        self._sent_by = None
        self._sent_to = None
        self._status = None
        self._subject = None
        self._update_request_id = None

        if props:
            deserialize(self, props)

        # requests package Response object
        self.request_response = None
        self.__initialized = True

    def __getattr__(self, key):
        if key == 'id':
            return self.id_
        else:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key == 'id':
            self.id_ = value
        else:
            super(SentUpdateRequest, self).__setattr__(key, value)

    @property
    def column_ids(self):
        return self._column_ids

    @column_ids.setter
    def column_ids(self, value):
        self._column_ids.load(value)

    @property
    def id_(self):
        return self._id_

    @id_.setter
    def id_(self, value):
        if isinstance(value, six.integer_types):
            self._id_ = value

    @property
    def include_attachments(self):
        return self._include_attachments

    @include_attachments.setter
    def include_attachments(self, value):
        if isinstance(value, bool):
            self._include_attachments = value

    @property
    def include_discussions(self):
        return self._include_discussions

    @include_discussions.setter
    def include_discussions(self, value):
        if isinstance(value, bool):
            self._include_discussions = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, six.string_types):
            self._message = value

    @property
    def row_ids(self):
        return self._row_ids

    @row_ids.setter
    def row_ids(self, value):
        self._row_ids.load(value)

    @property
    def sent_at(self):
        return self._sent_at

    @sent_at.setter
    def sent_at(self, value):
        if isinstance(value, datetime):
            self._sent_at = value
        else:
            if isinstance(value, six.string_types):
                value = parse(value)
                self._sent_at = value

    @property
    def sent_by(self):
        return self._sent_by

    @sent_by.setter
    def sent_by(self, value):
        if isinstance(value, User):
            self._sent_by = value
        else:
            if isinstance(value, dict):
                self._sent_by = User(value, self._base)

    @property
    def sent_to(self):
        return self._sent_to

    @sent_to.setter
    def sent_to(self, value):
        if isinstance(value, Recipient):
            self._sent_to = value
        elif isinstance(value, dict):
            self._sent_to = Recipient(value, self._base)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, six.string_types):
            if value not in self.allowed_values['update_request_status']:
                raise ValueError(
                    ("`{0}` is an invalid value for SentUpdateRequest`update_request_status`,"
                     " must be one of {1}").format(
                        value, self.allowed_values['update_request_status']))
            self._status = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, six.string_types):
            self._subject = value

    @property
    def update_request_id(self):
        return self._update_request_id

    @update_request_id.setter
    def update_request_id(self, value):
        if isinstance(value, six.integer_types):
            self._update_request_id = value

    def to_dict(self):
        return serialize(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
