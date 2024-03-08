"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2022 Flower Labs GmbH. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""
import builtins
import collections.abc
import flwr.proto.node_pb2
import flwr.proto.task_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CreateRunRequest(google.protobuf.message.Message):
    """CreateRun"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CreateRunRequest = CreateRunRequest

@typing_extensions.final
class CreateRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(
        self,
        *,
        run_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id", b"run_id"]) -> None: ...

global___CreateRunResponse = CreateRunResponse

@typing_extensions.final
class GetNodesRequest(google.protobuf.message.Message):
    """GetNodes messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(
        self,
        *,
        run_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id", b"run_id"]) -> None: ...

global___GetNodesRequest = GetNodesRequest

@typing_extensions.final
class GetNodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.node_pb2.Node]: ...
    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[flwr.proto.node_pb2.Node] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nodes", b"nodes"]) -> None: ...

global___GetNodesResponse = GetNodesResponse

@typing_extensions.final
class PushTaskInsRequest(google.protobuf.message.Message):
    """PushTaskIns messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_INS_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_ins_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskIns]: ...
    def __init__(
        self,
        *,
        task_ins_list: collections.abc.Iterable[flwr.proto.task_pb2.TaskIns] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ins_list", b"task_ins_list"]) -> None: ...

global___PushTaskInsRequest = PushTaskInsRequest

@typing_extensions.final
class PushTaskInsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        task_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ids", b"task_ids"]) -> None: ...

global___PushTaskInsResponse = PushTaskInsResponse

@typing_extensions.final
class PullTaskResRequest(google.protobuf.message.Message):
    """PullTaskRes messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_FIELD_NUMBER: builtins.int
    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        node: flwr.proto.node_pb2.Node | None = ...,
        task_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node", b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node", b"node", "task_ids", b"task_ids"]) -> None: ...

global___PullTaskResRequest = PullTaskResRequest

@typing_extensions.final
class PullTaskResResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_RES_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_res_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskRes]: ...
    def __init__(
        self,
        *,
        task_res_list: collections.abc.Iterable[flwr.proto.task_pb2.TaskRes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_res_list", b"task_res_list"]) -> None: ...

global___PullTaskResResponse = PullTaskResResponse
