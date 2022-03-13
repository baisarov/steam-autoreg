import enum


class Proxy(enum.IntEnum):
    Url = 1
    File = 2


class SelectionType(enum.IntEnum):
    RANDOM = 0
    CONSISTENT = 1


class SmsService(enum.IntEnum):
    OnlineSim = 0
    SmsActivate = 1


class CaptchaService(enum.IntEnum):
    RuCaptcha = 0
    AntiCaptcha = 1
