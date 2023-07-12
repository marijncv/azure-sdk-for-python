# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ChatMessageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The chat message type.
    """

    TEXT = "text"
    HTML = "html"
    TOPIC_UPDATED = "topicUpdated"
    PARTICIPANT_ADDED = "participantAdded"
    PARTICIPANT_REMOVED = "participantRemoved"

class CommunicationCloudEnvironmentModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The cloud that the identifier belongs to.
    """

    PUBLIC = "public"
    DOD = "dod"
    GCCH = "gcch"
