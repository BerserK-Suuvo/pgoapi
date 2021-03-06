# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import quest_type_pb2 as pogoprotos_dot_enums_dot_quest__type__pb2
from pogoprotos.data.quests import daily_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_daily__quest__pb2
from pogoprotos.data.quests import catch_pokemon_quest_pb2 as pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2
from pogoprotos.data.quests import quest_goal_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2
from pogoprotos.data.quests import quest_reward_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_pb=_b('\n\"pogoprotos/data/quests/quest.proto\x12\x16pogoprotos.data.quests\x1a!pogoprotos/enums/quest_type.proto\x1a(pogoprotos/data/quests/daily_quest.proto\x1a\x30pogoprotos/data/quests/catch_pokemon_quest.proto\x1a\'pogoprotos/data/quests/quest_goal.proto\x1a)pogoprotos/data/quests/quest_reward.proto\"\xb3\x06\n\x05Quest\x12/\n\nquest_type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.QuestType\x12\x37\n\x0b\x64\x61ily_quest\x18\x02 \x01(\x0b\x32\".pogoprotos.data.quests.DailyQuest\x12@\n\nmulti_part\x18\x03 \x01(\x0b\x32,.pogoprotos.data.quests.Quest.MultiPartQuest\x12@\n\rcatch_pokemon\x18\x04 \x01(\x0b\x32).pogoprotos.data.quests.CatchPokemonQuest\x12\x12\n\nquest_seed\x18\x64 \x01(\x03\x12<\n\rquest_context\x18\x65 \x01(\x0e\x32%.pogoprotos.data.quests.Quest.Context\x12\x13\n\x0btemplate_id\x18\x66 \x01(\t\x12\x10\n\x08progress\x18g \x01(\x05\x12/\n\x04goal\x18h \x01(\x0b\x32!.pogoprotos.data.quests.QuestGoal\x12\x34\n\x06status\x18i \x01(\x0e\x32$.pogoprotos.data.quests.Quest.Status\x12:\n\rquest_rewards\x18j \x03(\x0b\x32#.pogoprotos.data.quests.QuestReward\x12\x1d\n\x15\x63reation_timestamp_ms\x18k \x01(\x03\x12 \n\x18last_update_timestamp_ms\x18l \x01(\x03\x12 \n\x18\x63ompeletion_timestamp_ms\x18m \x01(\x03\x1a\x43\n\x0eMultiPartQuest\x12\x31\n\nsub_quests\x18\x01 \x03(\x0b\x32\x1d.pogoprotos.data.quests.Quest\"/\n\x07\x43ontext\x12\x0f\n\x0bSTORY_QUEST\x10\x00\x12\x13\n\x0f\x43HALLENGE_QUEST\x10\x01\"G\n\x06Status\x12\x14\n\x10STATUS_UNDEFINED\x10\x00\x12\x11\n\rSTATUS_ACTIVE\x10\x01\x12\x14\n\x10STATUS_COMPLETED\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_quest__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_daily__quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_QUEST_CONTEXT = _descriptor.EnumDescriptor(
  name='Context',
  full_name='pogoprotos.data.quests.Quest.Context',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORY_QUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=973,
  serialized_end=1020,
)
_sym_db.RegisterEnumDescriptor(_QUEST_CONTEXT)

_QUEST_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.data.quests.Quest.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_COMPLETED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1022,
  serialized_end=1093,
)
_sym_db.RegisterEnumDescriptor(_QUEST_STATUS)


_QUEST_MULTIPARTQUEST = _descriptor.Descriptor(
  name='MultiPartQuest',
  full_name='pogoprotos.data.quests.Quest.MultiPartQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_quests', full_name='pogoprotos.data.quests.Quest.MultiPartQuest.sub_quests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=904,
  serialized_end=971,
)

_QUEST = _descriptor.Descriptor(
  name='Quest',
  full_name='pogoprotos.data.quests.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_type', full_name='pogoprotos.data.quests.Quest.quest_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_quest', full_name='pogoprotos.data.quests.Quest.daily_quest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_part', full_name='pogoprotos.data.quests.Quest.multi_part', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catch_pokemon', full_name='pogoprotos.data.quests.Quest.catch_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_seed', full_name='pogoprotos.data.quests.Quest.quest_seed', index=4,
      number=100, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_context', full_name='pogoprotos.data.quests.Quest.quest_context', index=5,
      number=101, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='pogoprotos.data.quests.Quest.template_id', index=6,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='pogoprotos.data.quests.Quest.progress', index=7,
      number=103, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goal', full_name='pogoprotos.data.quests.Quest.goal', index=8,
      number=104, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.data.quests.Quest.status', index=9,
      number=105, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_rewards', full_name='pogoprotos.data.quests.Quest.quest_rewards', index=10,
      number=106, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='pogoprotos.data.quests.Quest.creation_timestamp_ms', index=11,
      number=107, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update_timestamp_ms', full_name='pogoprotos.data.quests.Quest.last_update_timestamp_ms', index=12,
      number=108, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compeletion_timestamp_ms', full_name='pogoprotos.data.quests.Quest.compeletion_timestamp_ms', index=13,
      number=109, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUEST_MULTIPARTQUEST, ],
  enum_types=[
    _QUEST_CONTEXT,
    _QUEST_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=1093,
)

_QUEST_MULTIPARTQUEST.fields_by_name['sub_quests'].message_type = _QUEST
_QUEST_MULTIPARTQUEST.containing_type = _QUEST
_QUEST.fields_by_name['quest_type'].enum_type = pogoprotos_dot_enums_dot_quest__type__pb2._QUESTTYPE
_QUEST.fields_by_name['daily_quest'].message_type = pogoprotos_dot_data_dot_quests_dot_daily__quest__pb2._DAILYQUEST
_QUEST.fields_by_name['multi_part'].message_type = _QUEST_MULTIPARTQUEST
_QUEST.fields_by_name['catch_pokemon'].message_type = pogoprotos_dot_data_dot_quests_dot_catch__pokemon__quest__pb2._CATCHPOKEMONQUEST
_QUEST.fields_by_name['quest_context'].enum_type = _QUEST_CONTEXT
_QUEST.fields_by_name['goal'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__goal__pb2._QUESTGOAL
_QUEST.fields_by_name['status'].enum_type = _QUEST_STATUS
_QUEST.fields_by_name['quest_rewards'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__reward__pb2._QUESTREWARD
_QUEST_CONTEXT.containing_type = _QUEST
_QUEST_STATUS.containing_type = _QUEST
DESCRIPTOR.message_types_by_name['Quest'] = _QUEST

Quest = _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), dict(

  MultiPartQuest = _reflection.GeneratedProtocolMessageType('MultiPartQuest', (_message.Message,), dict(
    DESCRIPTOR = _QUEST_MULTIPARTQUEST,
    __module__ = 'pogoprotos.data.quests.quest_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest.MultiPartQuest)
    ))
  ,
  DESCRIPTOR = _QUEST,
  __module__ = 'pogoprotos.data.quests.quest_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.Quest)
  ))
_sym_db.RegisterMessage(Quest)
_sym_db.RegisterMessage(Quest.MultiPartQuest)


# @@protoc_insertion_point(module_scope)
