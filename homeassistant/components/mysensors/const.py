"""MySensors constants."""

from __future__ import annotations

from collections import defaultdict
from typing import Final, Literal, TypedDict

from homeassistant.const import Platform

ATTR_DEVICES: Final = "devices"
ATTR_GATEWAY_ID: Final = "gateway_id"
ATTR_NODE_ID: Final = "node_id"

CONF_BAUD_RATE: Final = "baud_rate"
CONF_PERSISTENCE_FILE: Final = "persistence_file"
CONF_RETAIN: Final = "retain"
CONF_TCP_PORT: Final = "tcp_port"
CONF_TOPIC_IN_PREFIX: Final = "topic_in_prefix"
CONF_TOPIC_OUT_PREFIX: Final = "topic_out_prefix"
CONF_VERSION: Final = "version"
CONF_GATEWAY_TYPE: Final = "gateway_type"
type ConfGatewayType = Literal["Serial", "TCP", "MQTT"]
CONF_GATEWAY_TYPE_SERIAL: ConfGatewayType = "Serial"
CONF_GATEWAY_TYPE_TCP: ConfGatewayType = "TCP"
CONF_GATEWAY_TYPE_MQTT: ConfGatewayType = "MQTT"

DOMAIN: Final = "mysensors"
MYSENSORS_GATEWAY_START_TASK: str = "mysensors_gateway_start_task_{}"
MYSENSORS_GATEWAYS: Final = "mysensors_gateways"
MYSENSORS_DISCOVERED_NODES: Final = "mysensors_discovered_nodes_{}"
PLATFORM: Final = "platform"
SCHEMA: Final = "schema"
CHILD_CALLBACK: str = "mysensors_child_callback_{}_{}_{}_{}"
NODE_CALLBACK: str = "mysensors_node_callback_{}_{}"
MYSENSORS_DISCOVERY: str = "mysensors_discovery_{}_{}"
MYSENSORS_NODE_DISCOVERY: str = "mysensors_node_discovery"
MYSENSORS_ON_UNLOAD: str = "mysensors_on_unload_{}"
TYPE: Final = "type"
UPDATE_DELAY: float = 0.1


class DiscoveryInfo(TypedDict):
    """Represent the discovery info type for mysensors platforms."""

    devices: list[DevId]
    gateway_id: GatewayId


class NodeDiscoveryInfo(TypedDict):
    """Represent discovered mysensors node."""

    gateway_id: GatewayId
    node_id: int


SERVICE_SEND_IR_CODE: Final = "send_ir_code"

type SensorType = str
# S_DOOR, S_MOTION, S_SMOKE, ...

type ValueType = str
# V_TRIPPED, V_ARMED, V_STATUS, V_PERCENTAGE, ...

type GatewayId = str
# a unique id generated by config_flow.py and stored in the ConfigEntry as the entry id.

type DevId = tuple[GatewayId, int, int, int]
# describes the backend of a hass entity.
# Contents are: GatewayId, node_id, child_id, v_type as int
#
# The string version of v_type can be looked up in the enum gateway.const.SetReq
# of the appropriate BaseAsyncGateway
# Vioneta Agro Entities are quite limited and only ever do one thing.
# MySensors Nodes have multiple child_ids each with a s_type several associated v_types
# The MySensors integration brings these together by creating an entity for every v_type
# of every child_id of every node.
# The DevId tuple perfectly captures this.

BINARY_SENSOR_TYPES: dict[SensorType, set[ValueType]] = {
    "S_DOOR": {"V_TRIPPED"},
    "S_MOTION": {"V_TRIPPED"},
    "S_SMOKE": {"V_TRIPPED"},
    "S_SPRINKLER": {"V_TRIPPED"},
    "S_WATER_LEAK": {"V_TRIPPED"},
    "S_SOUND": {"V_TRIPPED"},
    "S_VIBRATION": {"V_TRIPPED"},
    "S_MOISTURE": {"V_TRIPPED"},
}

CLIMATE_TYPES: dict[SensorType, set[ValueType]] = {"S_HVAC": {"V_HVAC_FLOW_STATE"}}

COVER_TYPES: dict[SensorType, set[ValueType]] = {
    "S_COVER": {"V_DIMMER", "V_PERCENTAGE", "V_LIGHT", "V_STATUS"}
}

DEVICE_TRACKER_TYPES: dict[SensorType, set[ValueType]] = {"S_GPS": {"V_POSITION"}}

LIGHT_TYPES: dict[SensorType, set[ValueType]] = {
    "S_DIMMER": {"V_DIMMER", "V_PERCENTAGE"},
    "S_RGB_LIGHT": {"V_RGB"},
    "S_RGBW_LIGHT": {"V_RGBW"},
}

REMOTE_TYPES: dict[SensorType, set[ValueType]] = {"S_IR": {"V_IR_SEND"}}

SENSOR_TYPES: dict[SensorType, set[ValueType]] = {
    "S_SOUND": {"V_LEVEL"},
    "S_VIBRATION": {"V_LEVEL"},
    "S_MOISTURE": {"V_LEVEL"},
    "S_INFO": {"V_TEXT"},
    "S_GPS": {"V_POSITION"},
    "S_TEMP": {"V_TEMP"},
    "S_HUM": {"V_HUM"},
    "S_BARO": {"V_PRESSURE", "V_FORECAST"},
    "S_WIND": {"V_WIND", "V_GUST", "V_DIRECTION"},
    "S_RAIN": {"V_RAIN", "V_RAINRATE"},
    "S_UV": {"V_UV"},
    "S_WEIGHT": {"V_WEIGHT", "V_IMPEDANCE"},
    "S_POWER": {"V_WATT", "V_KWH", "V_VAR", "V_VA", "V_POWER_FACTOR"},
    "S_DISTANCE": {"V_DISTANCE"},
    "S_LIGHT_LEVEL": {"V_LIGHT_LEVEL", "V_LEVEL"},
    "S_IR": {"V_IR_RECEIVE", "V_IR_RECORD"},
    "S_WATER": {"V_FLOW", "V_VOLUME"},
    "S_CUSTOM": {"V_VAR1", "V_VAR2", "V_VAR3", "V_VAR4", "V_VAR5", "V_CUSTOM"},
    "S_SCENE_CONTROLLER": {"V_SCENE_ON", "V_SCENE_OFF"},
    "S_COLOR_SENSOR": {"V_RGB"},
    "S_MULTIMETER": {"V_VOLTAGE", "V_CURRENT", "V_IMPEDANCE"},
    "S_GAS": {"V_FLOW", "V_VOLUME"},
    "S_WATER_QUALITY": {"V_TEMP", "V_PH", "V_ORP", "V_EC"},
    "S_AIR_QUALITY": {"V_DUST_LEVEL", "V_LEVEL"},
    "S_DUST": {"V_DUST_LEVEL", "V_LEVEL"},
}

SWITCH_TYPES: dict[SensorType, set[ValueType]] = {
    "S_LIGHT": {"V_LIGHT"},
    "S_BINARY": {"V_STATUS"},
    "S_DOOR": {"V_ARMED"},
    "S_MOTION": {"V_ARMED"},
    "S_SMOKE": {"V_ARMED"},
    "S_SPRINKLER": {"V_STATUS"},
    "S_WATER_LEAK": {"V_ARMED"},
    "S_SOUND": {"V_ARMED"},
    "S_VIBRATION": {"V_ARMED"},
    "S_MOISTURE": {"V_ARMED"},
    "S_LOCK": {"V_LOCK_STATUS"},
    "S_WATER_QUALITY": {"V_STATUS"},
}

TEXT_TYPES: dict[SensorType, set[ValueType]] = {"S_INFO": {"V_TEXT"}}

PLATFORM_TYPES: dict[Platform, dict[SensorType, set[ValueType]]] = {
    Platform.BINARY_SENSOR: BINARY_SENSOR_TYPES,
    Platform.CLIMATE: CLIMATE_TYPES,
    Platform.COVER: COVER_TYPES,
    Platform.DEVICE_TRACKER: DEVICE_TRACKER_TYPES,
    Platform.LIGHT: LIGHT_TYPES,
    Platform.REMOTE: REMOTE_TYPES,
    Platform.SENSOR: SENSOR_TYPES,
    Platform.SWITCH: SWITCH_TYPES,
    Platform.TEXT: TEXT_TYPES,
}

FLAT_PLATFORM_TYPES: dict[tuple[str, SensorType], set[ValueType]] = {
    (platform, s_type_name): v_type_name
    for platform, platform_types in PLATFORM_TYPES.items()
    for s_type_name, v_type_name in platform_types.items()
}

TYPE_TO_PLATFORMS: dict[SensorType, list[Platform]] = defaultdict(list)

for platform, platform_types in PLATFORM_TYPES.items():
    for s_type_name in platform_types:
        TYPE_TO_PLATFORMS[s_type_name].append(platform)

PLATFORMS = tuple(PLATFORM_TYPES)
