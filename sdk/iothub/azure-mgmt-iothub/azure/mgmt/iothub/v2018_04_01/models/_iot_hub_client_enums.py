# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRights(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The permissions assigned to the shared access policy."""

    REGISTRY_READ = "RegistryRead"
    REGISTRY_WRITE = "RegistryWrite"
    SERVICE_CONNECT = "ServiceConnect"
    DEVICE_CONNECT = "DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE = "RegistryRead, RegistryWrite"
    REGISTRY_READ_SERVICE_CONNECT = "RegistryRead, ServiceConnect"
    REGISTRY_READ_DEVICE_CONNECT = "RegistryRead, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT = "RegistryWrite, ServiceConnect"
    REGISTRY_WRITE_DEVICE_CONNECT = "RegistryWrite, DeviceConnect"
    SERVICE_CONNECT_DEVICE_CONNECT = "ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect"
    REGISTRY_READ_REGISTRY_WRITE_DEVICE_CONNECT = "RegistryRead, RegistryWrite, DeviceConnect"
    REGISTRY_READ_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, ServiceConnect, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryWrite, ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = (
        "RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect"
    )


class Capabilities(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The capabilities and features enabled for the IoT hub."""

    NONE = "None"
    DEVICE_MANAGEMENT = "DeviceManagement"


class EndpointHealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The health status code of the endpoint."""

    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEAD = "dead"


class IotHubNameUnavailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for unavailability."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class IotHubScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the scaling enabled."""

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"


class IotHubSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU."""

    F1 = "F1"
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"


class IotHubSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The billing tier for the IoT hub."""

    FREE = "Free"
    STANDARD = "Standard"
    BASIC = "Basic"


class IpFilterActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The desired action for requests captured by this rule."""

    ACCEPT = "Accept"
    REJECT = "Reject"


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the job."""

    UNKNOWN = "unknown"
    ENQUEUED = "enqueued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the job."""

    UNKNOWN = "unknown"
    EXPORT = "export"
    IMPORT = "import"
    BACKUP = "backup"
    READ_DEVICE_PROPERTIES = "readDeviceProperties"
    WRITE_DEVICE_PROPERTIES = "writeDeviceProperties"
    UPDATE_DEVICE_CONFIGURATION = "updateDeviceConfiguration"
    REBOOT_DEVICE = "rebootDevice"
    FACTORY_RESET_DEVICE = "factoryResetDevice"
    FIRMWARE_UPDATE = "firmwareUpdate"
    IMPORT_ENUM = "import"


class OperationMonitoringLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operations monitoring level."""

    NONE = "None"
    ERROR = "Error"
    INFORMATION = "Information"
    ERROR_INFORMATION = "Error, Information"


class RouteErrorSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of the route error."""

    ERROR = "error"
    WARNING = "warning"


class RoutingSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The source that the routing rule is to be applied to, such as DeviceMessages."""

    INVALID = "Invalid"
    DEVICE_MESSAGES = "DeviceMessages"
    TWIN_CHANGE_EVENTS = "TwinChangeEvents"
    DEVICE_LIFECYCLE_EVENTS = "DeviceLifecycleEvents"
    DEVICE_JOB_LIFECYCLE_EVENTS = "DeviceJobLifecycleEvents"


class TestResultStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Result of testing route."""

    UNDEFINED = "undefined"
    FALSE = "false"
    TRUE = "true"
