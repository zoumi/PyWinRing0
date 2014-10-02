# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 csuodn <aaasuoliweng@126.com>
#
from ctypes import WinDLL, WINFUNCTYPE,c_ulong,c_ulonglong,c_byte
from ctypes.wintypes import BOOL, LONG, DWORD, POINT, PBYTE, PDWORD, DWORD,WORD,PWORD   #,BYTE
import sys

BYTE=c_byte

if "32 bit" in sys.version:
    DWORD_PTR=c_ulong
else:
    DWORD_PTR=c_ulonglong
VOID=None


winring0 = WinDLL("WinRing0")

def ErrCheck(result, func, args):
    if result:
        #raise RuntimeError('Calling function '+str(func)+' was not successful.Error code:'+hex(result))
        print('Calling function ' + func.FuncName +
              ' was not successful.\nError code:' + hex(result))
        #print(args)
    return args

def WRFun(name, dll, result, *args):
    '''myfunc = wfunc( '函数名',
                       DLL,
                       返回值类型,
                       (参数类型, '参数名', 参数方向，默认值),
                       (参数类型, '参数名', 参数方向，默认值)
                     )
    '''
    atypes = []
    aflags = []
    for arg in args:
        atypes.append(arg[0])
        aflags.append((arg[2], arg[1]) + arg[3:])
    func = WINFUNCTYPE(result, *atypes)((name, dll), tuple(aflags))
    #func.errcheck = ErrCheck
    func.FuncName = name
    return func


Cpuid = WRFun('Cpuid',
              winring0,
              BOOL,
              (DWORD, 'index', 1),
              (PDWORD, 'eax', 2),
              (PDWORD, 'ebx', 2),
              (PDWORD, 'ecx', 2),
              (PDWORD, 'edx', 2))

CpuidPx = WRFun('CpuidPx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'ebx', 2),
                (PDWORD, 'ecx', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'processAffinityMask', 1))

CpuidTx = WRFun('CpuidTx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'ebx', 2),
                (PDWORD, 'ecx', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'threadAffinityMask', 1))

DeinitializeOls = WRFun('DeinitializeOls',
                        winring0,
                        VOID)

FindPciDeviceByClass = WRFun('FindPciDeviceByClass',
                             winring0,
                             DWORD,
                             (BYTE, 'baseClass', 1),
                             (BYTE, 'subClass', 1),
                             (BYTE, 'programIf', 1),
                             (BYTE, 'index', 1))

FindPciDeviceById = WRFun('FindPciDeviceById',
                          winring0,
                          DWORD,
                          (WORD, 'vendorId', 1),
                          (WORD, 'deviceId', 1),
                          (BYTE, 'index', 1))

GetDllStatus = WRFun('GetDllStatus',
                     winring0,
                     DWORD)

GetDllVersion = WRFun('GetDllVersion',
                      winring0,
                      DWORD,
                      (PBYTE, 'major', 2),
                      (PBYTE, 'minor', 2),
                      (PBYTE, 'revision', 2),
                      (PBYTE, 'release', 2))

GetDriverType = WRFun('GetDriverType',
                      winring0,
                      DWORD)

GetDriverVersion = WRFun('GetDriverVersion',
                         winring0,
                         DWORD,
                         (PBYTE, 'major', 2),
                         (PBYTE, 'minor', 2),
                         (PBYTE, 'revision', 2),
                         (PBYTE, 'release', 2))

Hlt = WRFun('Hlt',
            winring0,
            BOOL)

HltPx = WRFun('HltPx',
              winring0,
              BOOL,
              (DWORD_PTR, 'processAffinityMask', 1))

HltTx = WRFun('HltTx',
              winring0,
              BOOL,
              (DWORD_PTR, 'threadAffinityMask', 1))

InitializeOls = WRFun('InitializeOls',
                      winring0,
                      BOOL)

IsCpuid = WRFun('IsCpuid',
                winring0,
                BOOL)

IsMsr = WRFun('IsMsr',
              winring0,
              BOOL)

IsTsc = WRFun('IsTsc',
              winring0,
              BOOL)

Rdmsr = WRFun('Rdmsr',
              winring0,
              BOOL,
              (DWORD, 'index', 1),
              (PDWORD, 'eax', 2),
              (PDWORD, 'edx', 2))

RdmsrPx = WRFun('RdmsrPx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'processAffinityMask', 1))

RdmsrTx = WRFun('RdmsrTx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'threadAffinityMask', 1))

Rdpmc = WRFun('Rdpmc',
              winring0,
              BOOL,
              (DWORD, 'index', 1),
              (PDWORD, 'eax', 2),
              (PDWORD, 'edx', 2))

RdpmcPx = WRFun('RdpmcPx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'processAffinityMask', 1))

RdpmcTx = WRFun('RdpmcTx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'threadAffinityMask', 1))

Rdtsc = WRFun('Rdtsc',
              winring0,
              BOOL,
              (PDWORD, 'eax', 2),
              (PDWORD, 'edx', 2))

RdtscPx = WRFun('RdtscPx',
                winring0,
                BOOL,
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'processAffinityMask', 1))

RdtscTx = WRFun('RdtscTx',
                winring0,
                BOOL,
                (PDWORD, 'eax', 2),
                (PDWORD, 'edx', 2),
                (DWORD_PTR, 'threadAffinityMask', 1))

ReadIoPortByte = WRFun('ReadIoPortByte',
                       winring0,
                       BYTE,
                       (WORD, 'port', 1))

ReadIoPortByteEx = WRFun('ReadIoPortByteEx',
                         winring0,
                         BOOL,
                         (WORD, 'port', 1),
                         (PBYTE, 'value', 2))

ReadIoPortDword = WRFun('ReadIoPortDword',
                        winring0,
                        DWORD,
                        (WORD, 'port', 1))

ReadIoPortDwordEx = WRFun('ReadIoPortDwordEx',
                          winring0,
                          BOOL,
                          (WORD, 'port', 1),
                          (PDWORD, 'value', 2))

ReadIoPortWord = WRFun('ReadIoPortWord',
                       winring0,
                       WORD,
                       (WORD, 'port', 1))

ReadIoPortWordEx = WRFun('ReadIoPortWordEx',
                         winring0,
                         BOOL,
                         (WORD, 'port', 1),
                         (PWORD, 'value', 2))

ReadPciConfigByte = WRFun('ReadPciConfigByte',
                          winring0,
                          BYTE,
                          (DWORD, 'pciAddress', 1),
                          (BYTE, 'regAddress', 1))

ReadPciConfigByteEx = WRFun('ReadPciConfigByteEx',
                            winring0,
                            BOOL,
                            (DWORD, 'pciAddress', 1),
                            (DWORD, 'regAddress', 1),
                            (PBYTE, 'value', 2))

ReadPciConfigDword = WRFun('ReadPciConfigDword',
                           winring0,
                           DWORD,
                           (DWORD, 'pciAddress', 1),
                           (BYTE, 'regAddress', 1))

ReadPciConfigDwordEx = WRFun('ReadPciConfigDwordEx',
                             winring0,
                             BOOL,
                             (DWORD, 'pciAddress', 1),
                             (DWORD, 'regAddress', 1),
                             (PDWORD, 'value', 2))

ReadPciConfigWord = WRFun('ReadPciConfigWord',
                          winring0,
                          WORD,
                          (DWORD, 'pciAddress', 1),
                          (BYTE, 'regAddress', 1))

ReadPciConfigWordEx = WRFun('ReadPciConfigWordEx',
                            winring0,
                            BOOL,
                            (DWORD, 'pciAddress', 1),
                            (DWORD, 'regAddress', 1),
                            (PWORD, 'value', 2))

SetPciMaxBusIndex = WRFun('SetPciMaxBusIndex',
                       winring0,
                       VOID,
                       (BYTE, 'max', 1))

WriteIoPortByte = WRFun('WriteIoPortByte',
                        winring0,
                        VOID,
                        (WORD, 'port', 1),
                        (BYTE, 'value', 1))

WriteIoPortByteEx = WRFun('WriteIoPortByteEx',
                          winring0,
                          BOOL,
                          (WORD, 'port', 1),
                          (BYTE, 'value', 1))

WriteIoPortDword = WRFun('WriteIoPortDword',
                         winring0,
                         VOID,
                         (WORD, 'port', 1),
                         (DWORD, 'value', 1))

WriteIoPortDwordEx = WRFun('WriteIoPortDwordEx',
                           winring0,
                           BOOL,
                           (WORD, 'port', 1),
                           (DWORD, 'value', 1))

WriteIoPortWord = WRFun('WriteIoPortWord',
                        winring0,
                        VOID,
                        (WORD, 'port', 1),
                        (WORD, 'value', 1))

WriteIoPortWordEx = WRFun('WriteIoPortWordEx',
                          winring0,
                          BOOL,
                          (WORD, 'port', 1),
                          (WORD, 'value', 1))

WritePciConfigByte = WRFun('WritePciConfigByte',
                           winring0,
                           VOID,
                           (DWORD, 'pciAddress', 1),
                           (BYTE, 'regAddress', 1),
                           (BYTE, 'value', 1))

WritePciConfigByteEx = WRFun('WritePciConfigByteEx',
                             winring0,
                             BOOL,
                             (DWORD, 'pciAddress', 1),
                             (DWORD, 'regAddress', 1),
                             (BYTE, 'value', 1))

WritePciConfigDword = WRFun('WritePciConfigDword',
                            winring0,
                            VOID,
                            (DWORD, 'pciAddress', 1),
                            (BYTE, 'regAddress', 1),
                            (DWORD, 'value', 1))

WritePciConfigDwordEx = WRFun('WritePciConfigDwordEx',
                              winring0,
                              BOOL,
                              (DWORD, 'pciAddress', 1),
                              (DWORD, 'regAddress', 1),
                              (DWORD, 'value', 1))

WritePciConfigWord = WRFun('WritePciConfigWord',
                           winring0,
                           VOID,
                           (DWORD, 'pciAddress', 1),
                           (BYTE, 'regAddress', 1),
                           (WORD, 'value', 1))

WritePciConfigWordEx = WRFun('WritePciConfigWordEx',
                             winring0,
                             BOOL,
                             (DWORD, 'pciAddress', 1),
                             (DWORD, 'regAddress', 1),
                             (WORD, 'value', 1))

Wrmsr = WRFun('Wrmsr',
              winring0,
              BOOL,
              (DWORD, 'index', 1),
              (DWORD, 'eax', 1),
              (DWORD, 'edx', 1))

WrmsrPx = WRFun('WrmsrPx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (DWORD, 'eax', 1),
                (DWORD, 'edx', 1),
                (DWORD_PTR, 'processAffinityMask', 1))

WrmsrTx = WRFun('WrmsrTx',
                winring0,
                BOOL,
                (DWORD, 'index', 1),
                (DWORD, 'eax', 1),
                (DWORD, 'edx', 1),
                (DWORD_PTR, 'threadAffinityMask', 1))