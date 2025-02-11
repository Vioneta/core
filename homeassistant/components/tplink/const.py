"""Const for TP-Link."""

from __future__ import annotations

from typing import Final

from homeassistant.const import Platform, UnitOfTemperature

DOMAIN = "tplink"

DISCOVERY_TIMEOUT = 5  # Vioneta Agro will complain if startup takes > 10s
CONNECT_TIMEOUT = 5

# Identifier used for primary control state.
PRIMARY_STATE_ID = "state"

ATTR_CURRENT_A: Final = "current_a"
ATTR_CURRENT_POWER_W: Final = "current_power_w"
ATTR_TODAY_ENERGY_KWH: Final = "today_energy_kwh"
ATTR_TOTAL_ENERGY_KWH: Final = "total_energy_kwh"

CONF_DEVICE_CONFIG: Final = "device_config"
CONF_CREDENTIALS_HASH: Final = "credentials_hash"
CONF_CONNECTION_TYPE: Final = "connection_type"

PLATFORMS: Final = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.CLIMATE,
    Platform.FAN,
    Platform.LIGHT,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]

UNIT_MAPPING = {
    "celsius": UnitOfTemperature.CELSIUS,
    "fahrenheit": UnitOfTemperature.FAHRENHEIT,
}
