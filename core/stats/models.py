# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flows(models.Model):
    id = models.BigAutoField(primary_key=True)
    octetdeltacount = models.BigIntegerField(db_column='octetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    packetdeltacount = models.BigIntegerField(db_column='packetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    deltaflowcount = models.BigIntegerField(db_column='deltaFlowCount', blank=True, null=True)  # Field name made lowercase.
    protocolidentifier = models.SmallIntegerField(db_column='protocolIdentifier', blank=True, null=True)  # Field name made lowercase.
    ipclassofservice = models.SmallIntegerField(db_column='ipClassOfService', blank=True, null=True)  # Field name made lowercase.
    tcpcontrolbits = models.IntegerField(db_column='tcpControlBits', blank=True, null=True)  # Field name made lowercase.
    sourcetransportport = models.IntegerField(db_column='sourceTransportPort', blank=True, null=True)  # Field name made lowercase.
    sourceipv4address = models.GenericIPAddressField(db_column='sourceIPv4Address', blank=True, null=True)  # Field name made lowercase.
    sourceipv4prefixlength = models.SmallIntegerField(db_column='sourceIPv4PrefixLength', blank=True, null=True)  # Field name made lowercase.
    ingressinterface = models.BigIntegerField(db_column='ingressInterface', blank=True, null=True)  # Field name made lowercase.
    destinationtransportport = models.IntegerField(db_column='destinationTransportPort', blank=True, null=True)  # Field name made lowercase.
    destinationipv4address = models.GenericIPAddressField(db_column='destinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    destinationipv4prefixlength = models.SmallIntegerField(db_column='destinationIPv4PrefixLength', blank=True, null=True)  # Field name made lowercase.
    egressinterface = models.BigIntegerField(db_column='egressInterface', blank=True, null=True)  # Field name made lowercase.
    ipnexthopipv4address = models.GenericIPAddressField(db_column='ipNextHopIPv4Address', blank=True, null=True)  # Field name made lowercase.
    bgpsourceasnumber = models.BigIntegerField(db_column='bgpSourceAsNumber', blank=True, null=True)  # Field name made lowercase.
    bgpdestinationasnumber = models.BigIntegerField(db_column='bgpDestinationAsNumber', blank=True, null=True)  # Field name made lowercase.
    bgpnexthopipv4address = models.GenericIPAddressField(db_column='bgpNextHopIPv4Address', blank=True, null=True)  # Field name made lowercase.
    postmcastpacketdeltacount = models.BigIntegerField(db_column='postMCastPacketDeltaCount', blank=True, null=True)  # Field name made lowercase.
    postmcastoctetdeltacount = models.BigIntegerField(db_column='postMCastOctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    flowendsysuptime = models.BigIntegerField(db_column='flowEndSysUpTime', blank=True, null=True)  # Field name made lowercase.
    flowstartsysuptime = models.BigIntegerField(db_column='flowStartSysUpTime', blank=True, null=True)  # Field name made lowercase.
    postoctetdeltacount = models.BigIntegerField(db_column='postOctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    postpacketdeltacount = models.BigIntegerField(db_column='postPacketDeltaCount', blank=True, null=True)  # Field name made lowercase.
    minimumiptotallength = models.BigIntegerField(db_column='minimumIpTotalLength', blank=True, null=True)  # Field name made lowercase.
    maximumiptotallength = models.BigIntegerField(db_column='maximumIpTotalLength', blank=True, null=True)  # Field name made lowercase.
    sourceipv6address = models.GenericIPAddressField(db_column='sourceIPv6Address', blank=True, null=True)  # Field name made lowercase.
    destinationipv6address = models.GenericIPAddressField(db_column='destinationIPv6Address', blank=True, null=True)  # Field name made lowercase.
    sourceipv6prefixlength = models.SmallIntegerField(db_column='sourceIPv6PrefixLength', blank=True, null=True)  # Field name made lowercase.
    destinationipv6prefixlength = models.SmallIntegerField(db_column='destinationIPv6PrefixLength', blank=True, null=True)  # Field name made lowercase.
    flowlabelipv6 = models.BigIntegerField(db_column='flowLabelIPv6', blank=True, null=True)  # Field name made lowercase.
    icmptypecodeipv4 = models.IntegerField(db_column='icmpTypeCodeIPv4', blank=True, null=True)  # Field name made lowercase.
    igmptype = models.SmallIntegerField(db_column='igmpType', blank=True, null=True)  # Field name made lowercase.
    samplinginterval = models.BigIntegerField(db_column='samplingInterval', blank=True, null=True)  # Field name made lowercase.
    samplingalgorithm = models.SmallIntegerField(db_column='samplingAlgorithm', blank=True, null=True)  # Field name made lowercase.
    flowactivetimeout = models.IntegerField(db_column='flowActiveTimeout', blank=True, null=True)  # Field name made lowercase.
    flowidletimeout = models.IntegerField(db_column='flowIdleTimeout', blank=True, null=True)  # Field name made lowercase.
    enginetype = models.SmallIntegerField(db_column='engineType', blank=True, null=True)  # Field name made lowercase.
    engineid = models.SmallIntegerField(db_column='engineId', blank=True, null=True)  # Field name made lowercase.
    exportedoctettotalcount = models.BigIntegerField(db_column='exportedOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    exportedmessagetotalcount = models.BigIntegerField(db_column='exportedMessageTotalCount', blank=True, null=True)  # Field name made lowercase.
    exportedflowrecordtotalcount = models.BigIntegerField(db_column='exportedFlowRecordTotalCount', blank=True, null=True)  # Field name made lowercase.
    ipv4routersc = models.GenericIPAddressField(db_column='ipv4RouterSc', blank=True, null=True)  # Field name made lowercase.
    sourceipv4prefix = models.GenericIPAddressField(db_column='sourceIPv4Prefix', blank=True, null=True)  # Field name made lowercase.
    destinationipv4prefix = models.GenericIPAddressField(db_column='destinationIPv4Prefix', blank=True, null=True)  # Field name made lowercase.
    mplstoplabeltype = models.SmallIntegerField(db_column='mplsTopLabelType', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelipv4address = models.GenericIPAddressField(db_column='mplsTopLabelIPv4Address', blank=True, null=True)  # Field name made lowercase.
    samplerid = models.SmallIntegerField(db_column='samplerId', blank=True, null=True)  # Field name made lowercase.
    samplermode = models.SmallIntegerField(db_column='samplerMode', blank=True, null=True)  # Field name made lowercase.
    samplerrandominterval = models.BigIntegerField(db_column='samplerRandomInterval', blank=True, null=True)  # Field name made lowercase.
    classid = models.SmallIntegerField(db_column='classId', blank=True, null=True)  # Field name made lowercase.
    minimumttl = models.SmallIntegerField(db_column='minimumTTL', blank=True, null=True)  # Field name made lowercase.
    maximumttl = models.SmallIntegerField(db_column='maximumTTL', blank=True, null=True)  # Field name made lowercase.
    fragmentidentification = models.BigIntegerField(db_column='fragmentIdentification', blank=True, null=True)  # Field name made lowercase.
    postipclassofservice = models.SmallIntegerField(db_column='postIpClassOfService', blank=True, null=True)  # Field name made lowercase.
    sourcemacaddress = models.TextField(db_column='sourceMacAddress', blank=True, null=True)  # Field name made lowercase.
    postdestinationmacaddress = models.TextField(db_column='postDestinationMacAddress', blank=True, null=True)  # Field name made lowercase.
    vlanid = models.IntegerField(db_column='vlanId', blank=True, null=True)  # Field name made lowercase.
    postvlanid = models.IntegerField(db_column='postVlanId', blank=True, null=True)  # Field name made lowercase.
    ipversion = models.SmallIntegerField(db_column='ipVersion', blank=True, null=True)  # Field name made lowercase.
    flowdirection = models.SmallIntegerField(db_column='flowDirection', blank=True, null=True)  # Field name made lowercase.
    ipnexthopipv6address = models.GenericIPAddressField(db_column='ipNextHopIPv6Address', blank=True, null=True)  # Field name made lowercase.
    bgpnexthopipv6address = models.GenericIPAddressField(db_column='bgpNextHopIPv6Address', blank=True, null=True)  # Field name made lowercase.
    ipv6extensionheaders = models.BigIntegerField(db_column='ipv6ExtensionHeaders', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelstacksection = models.TextField(db_column='mplsTopLabelStackSection', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection2 = models.TextField(db_column='mplsLabelStackSection2', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection3 = models.TextField(db_column='mplsLabelStackSection3', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection4 = models.TextField(db_column='mplsLabelStackSection4', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection5 = models.TextField(db_column='mplsLabelStackSection5', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection6 = models.TextField(db_column='mplsLabelStackSection6', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection7 = models.TextField(db_column='mplsLabelStackSection7', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection8 = models.TextField(db_column='mplsLabelStackSection8', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection9 = models.TextField(db_column='mplsLabelStackSection9', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection10 = models.TextField(db_column='mplsLabelStackSection10', blank=True, null=True)  # Field name made lowercase.
    destinationmacaddress = models.TextField(db_column='destinationMacAddress', blank=True, null=True)  # Field name made lowercase.
    postsourcemacaddress = models.TextField(db_column='postSourceMacAddress', blank=True, null=True)  # Field name made lowercase.
    interfacename = models.TextField(db_column='interfaceName', blank=True, null=True)  # Field name made lowercase.
    interfacedescription = models.TextField(db_column='interfaceDescription', blank=True, null=True)  # Field name made lowercase.
    samplername = models.TextField(db_column='samplerName', blank=True, null=True)  # Field name made lowercase.
    octettotalcount = models.BigIntegerField(db_column='octetTotalCount', blank=True, null=True)  # Field name made lowercase.
    packettotalcount = models.BigIntegerField(db_column='packetTotalCount', blank=True, null=True)  # Field name made lowercase.
    flagsandsamplerid = models.BigIntegerField(db_column='flagsAndSamplerId', blank=True, null=True)  # Field name made lowercase.
    fragmentoffset = models.IntegerField(db_column='fragmentOffset', blank=True, null=True)  # Field name made lowercase.
    forwardingstatus = models.BigIntegerField(db_column='forwardingStatus', blank=True, null=True)  # Field name made lowercase.
    mplsvpnroutedistinguisher = models.TextField(db_column='mplsVpnRouteDistinguisher', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelprefixlength = models.SmallIntegerField(db_column='mplsTopLabelPrefixLength', blank=True, null=True)  # Field name made lowercase.
    srctrafficindex = models.BigIntegerField(db_column='srcTrafficIndex', blank=True, null=True)  # Field name made lowercase.
    dsttrafficindex = models.BigIntegerField(db_column='dstTrafficIndex', blank=True, null=True)  # Field name made lowercase.
    applicationdescription = models.TextField(db_column='applicationDescription', blank=True, null=True)  # Field name made lowercase.
    applicationid = models.TextField(db_column='applicationId', blank=True, null=True)  # Field name made lowercase.
    applicationname = models.TextField(db_column='applicationName', blank=True, null=True)  # Field name made lowercase.
    postipdiffservcodepoint = models.SmallIntegerField(db_column='postIpDiffServCodePoint', blank=True, null=True)  # Field name made lowercase.
    multicastreplicationfactor = models.BigIntegerField(db_column='multicastReplicationFactor', blank=True, null=True)  # Field name made lowercase.
    classname = models.TextField(db_column='className', blank=True, null=True)  # Field name made lowercase.
    classificationengineid = models.SmallIntegerField(db_column='classificationEngineId', blank=True, null=True)  # Field name made lowercase.
    layer2packetsectionoffset = models.IntegerField(db_column='layer2packetSectionOffset', blank=True, null=True)  # Field name made lowercase.
    layer2packetsectionsize = models.IntegerField(db_column='layer2packetSectionSize', blank=True, null=True)  # Field name made lowercase.
    layer2packetsectiondata = models.TextField(db_column='layer2packetSectionData', blank=True, null=True)  # Field name made lowercase.
    bgpnextadjacentasnumber = models.BigIntegerField(db_column='bgpNextAdjacentAsNumber', blank=True, null=True)  # Field name made lowercase.
    bgpprevadjacentasnumber = models.BigIntegerField(db_column='bgpPrevAdjacentAsNumber', blank=True, null=True)  # Field name made lowercase.
    exporteripv4address = models.GenericIPAddressField(db_column='exporterIPv4Address', blank=True, null=True)  # Field name made lowercase.
    exporteripv6address = models.GenericIPAddressField(db_column='exporterIPv6Address', blank=True, null=True)  # Field name made lowercase.
    droppedoctetdeltacount = models.BigIntegerField(db_column='droppedOctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    droppedpacketdeltacount = models.BigIntegerField(db_column='droppedPacketDeltaCount', blank=True, null=True)  # Field name made lowercase.
    droppedoctettotalcount = models.BigIntegerField(db_column='droppedOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    droppedpackettotalcount = models.BigIntegerField(db_column='droppedPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    flowendreason = models.SmallIntegerField(db_column='flowEndReason', blank=True, null=True)  # Field name made lowercase.
    commonpropertiesid = models.BigIntegerField(db_column='commonPropertiesId', blank=True, null=True)  # Field name made lowercase.
    observationpointid = models.BigIntegerField(db_column='observationPointId', blank=True, null=True)  # Field name made lowercase.
    icmptypecodeipv6 = models.IntegerField(db_column='icmpTypeCodeIPv6', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelipv6address = models.GenericIPAddressField(db_column='mplsTopLabelIPv6Address', blank=True, null=True)  # Field name made lowercase.
    linecardid = models.BigIntegerField(db_column='lineCardId', blank=True, null=True)  # Field name made lowercase.
    portid = models.BigIntegerField(db_column='portId', blank=True, null=True)  # Field name made lowercase.
    meteringprocessid = models.BigIntegerField(db_column='meteringProcessId', blank=True, null=True)  # Field name made lowercase.
    exportingprocessid = models.BigIntegerField(db_column='exportingProcessId', blank=True, null=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='templateId', blank=True, null=True)  # Field name made lowercase.
    wlanchannelid = models.SmallIntegerField(db_column='wlanChannelId', blank=True, null=True)  # Field name made lowercase.
    wlanssid = models.TextField(db_column='wlanSSID', blank=True, null=True)  # Field name made lowercase.
    flowid = models.BigIntegerField(db_column='flowId', blank=True, null=True)  # Field name made lowercase.
    observationdomainid = models.BigIntegerField(db_column='observationDomainId', blank=True, null=True)  # Field name made lowercase.
    flowstartseconds = models.BigIntegerField(db_column='flowStartSeconds', blank=True, null=True)  # Field name made lowercase.
    flowendseconds = models.BigIntegerField(db_column='flowEndSeconds', blank=True, null=True)  # Field name made lowercase.
    flowstartmilliseconds = models.BigIntegerField(db_column='flowStartMilliseconds', blank=True, null=True)  # Field name made lowercase.
    flowendmilliseconds = models.BigIntegerField(db_column='flowEndMilliseconds', blank=True, null=True)  # Field name made lowercase.
    flowstartmicroseconds = models.BigIntegerField(db_column='flowStartMicroseconds', blank=True, null=True)  # Field name made lowercase.
    flowendmicroseconds = models.BigIntegerField(db_column='flowEndMicroseconds', blank=True, null=True)  # Field name made lowercase.
    flowstartnanoseconds = models.BigIntegerField(db_column='flowStartNanoseconds', blank=True, null=True)  # Field name made lowercase.
    flowendnanoseconds = models.BigIntegerField(db_column='flowEndNanoseconds', blank=True, null=True)  # Field name made lowercase.
    flowstartdeltamicroseconds = models.BigIntegerField(db_column='flowStartDeltaMicroseconds', blank=True, null=True)  # Field name made lowercase.
    flowenddeltamicroseconds = models.BigIntegerField(db_column='flowEndDeltaMicroseconds', blank=True, null=True)  # Field name made lowercase.
    systeminittimemilliseconds = models.BigIntegerField(db_column='systemInitTimeMilliseconds', blank=True, null=True)  # Field name made lowercase.
    flowdurationmilliseconds = models.BigIntegerField(db_column='flowDurationMilliseconds', blank=True, null=True)  # Field name made lowercase.
    flowdurationmicroseconds = models.BigIntegerField(db_column='flowDurationMicroseconds', blank=True, null=True)  # Field name made lowercase.
    observedflowtotalcount = models.BigIntegerField(db_column='observedFlowTotalCount', blank=True, null=True)  # Field name made lowercase.
    ignoredpackettotalcount = models.BigIntegerField(db_column='ignoredPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    ignoredoctettotalcount = models.BigIntegerField(db_column='ignoredOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    notsentflowtotalcount = models.BigIntegerField(db_column='notSentFlowTotalCount', blank=True, null=True)  # Field name made lowercase.
    notsentpackettotalcount = models.BigIntegerField(db_column='notSentPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    notsentoctettotalcount = models.BigIntegerField(db_column='notSentOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    destinationipv6prefix = models.GenericIPAddressField(db_column='destinationIPv6Prefix', blank=True, null=True)  # Field name made lowercase.
    sourceipv6prefix = models.GenericIPAddressField(db_column='sourceIPv6Prefix', blank=True, null=True)  # Field name made lowercase.
    postoctettotalcount = models.BigIntegerField(db_column='postOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    postpackettotalcount = models.BigIntegerField(db_column='postPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    flowkeyindicator = models.BigIntegerField(db_column='flowKeyIndicator', blank=True, null=True)  # Field name made lowercase.
    postmcastpackettotalcount = models.BigIntegerField(db_column='postMCastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    postmcastoctettotalcount = models.BigIntegerField(db_column='postMCastOctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    icmptypeipv4 = models.SmallIntegerField(db_column='icmpTypeIPv4', blank=True, null=True)  # Field name made lowercase.
    icmpcodeipv4 = models.SmallIntegerField(db_column='icmpCodeIPv4', blank=True, null=True)  # Field name made lowercase.
    icmptypeipv6 = models.SmallIntegerField(db_column='icmpTypeIPv6', blank=True, null=True)  # Field name made lowercase.
    icmpcodeipv6 = models.SmallIntegerField(db_column='icmpCodeIPv6', blank=True, null=True)  # Field name made lowercase.
    udpsourceport = models.IntegerField(db_column='udpSourcePort', blank=True, null=True)  # Field name made lowercase.
    udpdestinationport = models.IntegerField(db_column='udpDestinationPort', blank=True, null=True)  # Field name made lowercase.
    tcpsourceport = models.IntegerField(db_column='tcpSourcePort', blank=True, null=True)  # Field name made lowercase.
    tcpdestinationport = models.IntegerField(db_column='tcpDestinationPort', blank=True, null=True)  # Field name made lowercase.
    tcpsequencenumber = models.BigIntegerField(db_column='tcpSequenceNumber', blank=True, null=True)  # Field name made lowercase.
    tcpacknowledgementnumber = models.BigIntegerField(db_column='tcpAcknowledgementNumber', blank=True, null=True)  # Field name made lowercase.
    tcpwindowsize = models.IntegerField(db_column='tcpWindowSize', blank=True, null=True)  # Field name made lowercase.
    tcpurgentpointer = models.IntegerField(db_column='tcpUrgentPointer', blank=True, null=True)  # Field name made lowercase.
    tcpheaderlength = models.SmallIntegerField(db_column='tcpHeaderLength', blank=True, null=True)  # Field name made lowercase.
    ipheaderlength = models.SmallIntegerField(db_column='ipHeaderLength', blank=True, null=True)  # Field name made lowercase.
    totallengthipv4 = models.IntegerField(db_column='totalLengthIPv4', blank=True, null=True)  # Field name made lowercase.
    payloadlengthipv6 = models.IntegerField(db_column='payloadLengthIPv6', blank=True, null=True)  # Field name made lowercase.
    ipttl = models.SmallIntegerField(db_column='ipTTL', blank=True, null=True)  # Field name made lowercase.
    nextheaderipv6 = models.SmallIntegerField(db_column='nextHeaderIPv6', blank=True, null=True)  # Field name made lowercase.
    mplspayloadlength = models.BigIntegerField(db_column='mplsPayloadLength', blank=True, null=True)  # Field name made lowercase.
    ipdiffservcodepoint = models.SmallIntegerField(db_column='ipDiffServCodePoint', blank=True, null=True)  # Field name made lowercase.
    ipprecedence = models.SmallIntegerField(db_column='ipPrecedence', blank=True, null=True)  # Field name made lowercase.
    fragmentflags = models.SmallIntegerField(db_column='fragmentFlags', blank=True, null=True)  # Field name made lowercase.
    octetdeltasumofsquares = models.BigIntegerField(db_column='octetDeltaSumOfSquares', blank=True, null=True)  # Field name made lowercase.
    octettotalsumofsquares = models.BigIntegerField(db_column='octetTotalSumOfSquares', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelttl = models.SmallIntegerField(db_column='mplsTopLabelTTL', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacklength = models.BigIntegerField(db_column='mplsLabelStackLength', blank=True, null=True)  # Field name made lowercase.
    mplslabelstackdepth = models.BigIntegerField(db_column='mplsLabelStackDepth', blank=True, null=True)  # Field name made lowercase.
    mplstoplabelexp = models.SmallIntegerField(db_column='mplsTopLabelExp', blank=True, null=True)  # Field name made lowercase.
    ippayloadlength = models.BigIntegerField(db_column='ipPayloadLength', blank=True, null=True)  # Field name made lowercase.
    udpmessagelength = models.IntegerField(db_column='udpMessageLength', blank=True, null=True)  # Field name made lowercase.
    ismulticast = models.SmallIntegerField(db_column='isMulticast', blank=True, null=True)  # Field name made lowercase.
    ipv4ihl = models.SmallIntegerField(db_column='ipv4IHL', blank=True, null=True)  # Field name made lowercase.
    ipv4options = models.BigIntegerField(db_column='ipv4Options', blank=True, null=True)  # Field name made lowercase.
    tcpoptions = models.BigIntegerField(db_column='tcpOptions', blank=True, null=True)  # Field name made lowercase.
    paddingoctets = models.TextField(db_column='paddingOctets', blank=True, null=True)  # Field name made lowercase.
    collectoripv4address = models.GenericIPAddressField(db_column='collectorIPv4Address', blank=True, null=True)  # Field name made lowercase.
    collectoripv6address = models.GenericIPAddressField(db_column='collectorIPv6Address', blank=True, null=True)  # Field name made lowercase.
    exportinterface = models.BigIntegerField(db_column='exportInterface', blank=True, null=True)  # Field name made lowercase.
    exportprotocolversion = models.SmallIntegerField(db_column='exportProtocolVersion', blank=True, null=True)  # Field name made lowercase.
    exporttransportprotocol = models.SmallIntegerField(db_column='exportTransportProtocol', blank=True, null=True)  # Field name made lowercase.
    collectortransportport = models.IntegerField(db_column='collectorTransportPort', blank=True, null=True)  # Field name made lowercase.
    exportertransportport = models.IntegerField(db_column='exporterTransportPort', blank=True, null=True)  # Field name made lowercase.
    tcpsyntotalcount = models.BigIntegerField(db_column='tcpSynTotalCount', blank=True, null=True)  # Field name made lowercase.
    tcpfintotalcount = models.BigIntegerField(db_column='tcpFinTotalCount', blank=True, null=True)  # Field name made lowercase.
    tcprsttotalcount = models.BigIntegerField(db_column='tcpRstTotalCount', blank=True, null=True)  # Field name made lowercase.
    tcppshtotalcount = models.BigIntegerField(db_column='tcpPshTotalCount', blank=True, null=True)  # Field name made lowercase.
    tcpacktotalcount = models.BigIntegerField(db_column='tcpAckTotalCount', blank=True, null=True)  # Field name made lowercase.
    tcpurgtotalcount = models.BigIntegerField(db_column='tcpUrgTotalCount', blank=True, null=True)  # Field name made lowercase.
    iptotallength = models.BigIntegerField(db_column='ipTotalLength', blank=True, null=True)  # Field name made lowercase.
    postnatsourceipv4address = models.GenericIPAddressField(db_column='postNATSourceIPv4Address', blank=True, null=True)  # Field name made lowercase.
    postnatdestinationipv4address = models.GenericIPAddressField(db_column='postNATDestinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    postnaptsourcetransportport = models.IntegerField(db_column='postNAPTSourceTransportPort', blank=True, null=True)  # Field name made lowercase.
    postnaptdestinationtransportport = models.IntegerField(db_column='postNAPTDestinationTransportPort', blank=True, null=True)  # Field name made lowercase.
    natoriginatingaddressrealm = models.SmallIntegerField(db_column='natOriginatingAddressRealm', blank=True, null=True)  # Field name made lowercase.
    natevent = models.SmallIntegerField(db_column='natEvent', blank=True, null=True)  # Field name made lowercase.
    initiatoroctets = models.BigIntegerField(db_column='initiatorOctets', blank=True, null=True)  # Field name made lowercase.
    responderoctets = models.BigIntegerField(db_column='responderOctets', blank=True, null=True)  # Field name made lowercase.
    firewallevent = models.SmallIntegerField(db_column='firewallEvent', blank=True, null=True)  # Field name made lowercase.
    ingressvrfid = models.BigIntegerField(db_column='ingressVRFID', blank=True, null=True)  # Field name made lowercase.
    egressvrfid = models.BigIntegerField(db_column='egressVRFID', blank=True, null=True)  # Field name made lowercase.
    vrfname = models.TextField(db_column='VRFname', blank=True, null=True)  # Field name made lowercase.
    postmplstoplabelexp = models.SmallIntegerField(db_column='postMplsTopLabelExp', blank=True, null=True)  # Field name made lowercase.
    tcpwindowscale = models.IntegerField(db_column='tcpWindowScale', blank=True, null=True)  # Field name made lowercase.
    biflowdirection = models.SmallIntegerField(db_column='biflowDirection', blank=True, null=True)  # Field name made lowercase.
    ethernetheaderlength = models.SmallIntegerField(db_column='ethernetHeaderLength', blank=True, null=True)  # Field name made lowercase.
    ethernetpayloadlength = models.IntegerField(db_column='ethernetPayloadLength', blank=True, null=True)  # Field name made lowercase.
    ethernettotallength = models.IntegerField(db_column='ethernetTotalLength', blank=True, null=True)  # Field name made lowercase.
    dot1qvlanid = models.IntegerField(db_column='dot1qVlanId', blank=True, null=True)  # Field name made lowercase.
    dot1qpriority = models.SmallIntegerField(db_column='dot1qPriority', blank=True, null=True)  # Field name made lowercase.
    dot1qcustomervlanid = models.IntegerField(db_column='dot1qCustomerVlanId', blank=True, null=True)  # Field name made lowercase.
    dot1qcustomerpriority = models.SmallIntegerField(db_column='dot1qCustomerPriority', blank=True, null=True)  # Field name made lowercase.
    metroevcid = models.TextField(db_column='metroEvcId', blank=True, null=True)  # Field name made lowercase.
    metroevctype = models.SmallIntegerField(db_column='metroEvcType', blank=True, null=True)  # Field name made lowercase.
    pseudowireid = models.BigIntegerField(db_column='pseudoWireId', blank=True, null=True)  # Field name made lowercase.
    pseudowiretype = models.IntegerField(db_column='pseudoWireType', blank=True, null=True)  # Field name made lowercase.
    pseudowirecontrolword = models.BigIntegerField(db_column='pseudoWireControlWord', blank=True, null=True)  # Field name made lowercase.
    ingressphysicalinterface = models.BigIntegerField(db_column='ingressPhysicalInterface', blank=True, null=True)  # Field name made lowercase.
    egressphysicalinterface = models.BigIntegerField(db_column='egressPhysicalInterface', blank=True, null=True)  # Field name made lowercase.
    postdot1qvlanid = models.IntegerField(db_column='postDot1qVlanId', blank=True, null=True)  # Field name made lowercase.
    postdot1qcustomervlanid = models.IntegerField(db_column='postDot1qCustomerVlanId', blank=True, null=True)  # Field name made lowercase.
    ethernettype = models.IntegerField(db_column='ethernetType', blank=True, null=True)  # Field name made lowercase.
    postipprecedence = models.SmallIntegerField(db_column='postIpPrecedence', blank=True, null=True)  # Field name made lowercase.
    collectiontimemilliseconds = models.BigIntegerField(db_column='collectionTimeMilliseconds', blank=True, null=True)  # Field name made lowercase.
    exportsctpstreamid = models.IntegerField(db_column='exportSctpStreamId', blank=True, null=True)  # Field name made lowercase.
    maxexportseconds = models.BigIntegerField(db_column='maxExportSeconds', blank=True, null=True)  # Field name made lowercase.
    maxflowendseconds = models.BigIntegerField(db_column='maxFlowEndSeconds', blank=True, null=True)  # Field name made lowercase.
    messagemd5checksum = models.TextField(db_column='messageMD5Checksum', blank=True, null=True)  # Field name made lowercase.
    messagescope = models.SmallIntegerField(db_column='messageScope', blank=True, null=True)  # Field name made lowercase.
    minexportseconds = models.BigIntegerField(db_column='minExportSeconds', blank=True, null=True)  # Field name made lowercase.
    minflowstartseconds = models.BigIntegerField(db_column='minFlowStartSeconds', blank=True, null=True)  # Field name made lowercase.
    opaqueoctets = models.TextField(db_column='opaqueOctets', blank=True, null=True)  # Field name made lowercase.
    sessionscope = models.SmallIntegerField(db_column='sessionScope', blank=True, null=True)  # Field name made lowercase.
    maxflowendmicroseconds = models.BigIntegerField(db_column='maxFlowEndMicroseconds', blank=True, null=True)  # Field name made lowercase.
    maxflowendmilliseconds = models.BigIntegerField(db_column='maxFlowEndMilliseconds', blank=True, null=True)  # Field name made lowercase.
    maxflowendnanoseconds = models.BigIntegerField(db_column='maxFlowEndNanoseconds', blank=True, null=True)  # Field name made lowercase.
    minflowstartmicroseconds = models.BigIntegerField(db_column='minFlowStartMicroseconds', blank=True, null=True)  # Field name made lowercase.
    minflowstartmilliseconds = models.BigIntegerField(db_column='minFlowStartMilliseconds', blank=True, null=True)  # Field name made lowercase.
    minflowstartnanoseconds = models.BigIntegerField(db_column='minFlowStartNanoseconds', blank=True, null=True)  # Field name made lowercase.
    collectorcertificate = models.TextField(db_column='collectorCertificate', blank=True, null=True)  # Field name made lowercase.
    exportercertificate = models.TextField(db_column='exporterCertificate', blank=True, null=True)  # Field name made lowercase.
    datarecordsreliability = models.BooleanField(db_column='dataRecordsReliability', blank=True, null=True)  # Field name made lowercase.
    observationpointtype = models.SmallIntegerField(db_column='observationPointType', blank=True, null=True)  # Field name made lowercase.
    newconnectiondeltacount = models.BigIntegerField(db_column='newConnectionDeltaCount', blank=True, null=True)  # Field name made lowercase.
    connectionsumdurationseconds = models.BigIntegerField(db_column='connectionSumDurationSeconds', blank=True, null=True)  # Field name made lowercase.
    connectiontransactionid = models.BigIntegerField(db_column='connectionTransactionId', blank=True, null=True)  # Field name made lowercase.
    postnatsourceipv6address = models.GenericIPAddressField(db_column='postNATSourceIPv6Address', blank=True, null=True)  # Field name made lowercase.
    postnatdestinationipv6address = models.GenericIPAddressField(db_column='postNATDestinationIPv6Address', blank=True, null=True)  # Field name made lowercase.
    natpoolid = models.BigIntegerField(db_column='natPoolId', blank=True, null=True)  # Field name made lowercase.
    natpoolname = models.TextField(db_column='natPoolName', blank=True, null=True)  # Field name made lowercase.
    anonymizationflags = models.IntegerField(db_column='anonymizationFlags', blank=True, null=True)  # Field name made lowercase.
    anonymizationtechnique = models.IntegerField(db_column='anonymizationTechnique', blank=True, null=True)  # Field name made lowercase.
    informationelementindex = models.IntegerField(db_column='informationElementIndex', blank=True, null=True)  # Field name made lowercase.
    p2ptechnology = models.TextField(db_column='p2pTechnology', blank=True, null=True)  # Field name made lowercase.
    tunneltechnology = models.TextField(db_column='tunnelTechnology', blank=True, null=True)  # Field name made lowercase.
    encryptedtechnology = models.TextField(db_column='encryptedTechnology', blank=True, null=True)  # Field name made lowercase.
    basiclist = models.TextField(db_column='basicList', blank=True, null=True)  # Field name made lowercase.
    subtemplatelist = models.TextField(db_column='subTemplateList', blank=True, null=True)  # Field name made lowercase.
    subtemplatemultilist = models.TextField(db_column='subTemplateMultiList', blank=True, null=True)  # Field name made lowercase.
    bgpvaliditystate = models.SmallIntegerField(db_column='bgpValidityState', blank=True, null=True)  # Field name made lowercase.
    ipsecspi = models.BigIntegerField(db_column='IPSecSPI', blank=True, null=True)  # Field name made lowercase.
    grekey = models.BigIntegerField(db_column='greKey', blank=True, null=True)  # Field name made lowercase.
    nattype = models.SmallIntegerField(db_column='natType', blank=True, null=True)  # Field name made lowercase.
    initiatorpackets = models.BigIntegerField(db_column='initiatorPackets', blank=True, null=True)  # Field name made lowercase.
    responderpackets = models.BigIntegerField(db_column='responderPackets', blank=True, null=True)  # Field name made lowercase.
    observationdomainname = models.TextField(db_column='observationDomainName', blank=True, null=True)  # Field name made lowercase.
    selectionsequenceid = models.BigIntegerField(db_column='selectionSequenceId', blank=True, null=True)  # Field name made lowercase.
    selectorid = models.BigIntegerField(db_column='selectorId', blank=True, null=True)  # Field name made lowercase.
    informationelementid = models.IntegerField(db_column='informationElementId', blank=True, null=True)  # Field name made lowercase.
    selectoralgorithm = models.IntegerField(db_column='selectorAlgorithm', blank=True, null=True)  # Field name made lowercase.
    samplingpacketinterval = models.BigIntegerField(db_column='samplingPacketInterval', blank=True, null=True)  # Field name made lowercase.
    samplingpacketspace = models.BigIntegerField(db_column='samplingPacketSpace', blank=True, null=True)  # Field name made lowercase.
    samplingtimeinterval = models.BigIntegerField(db_column='samplingTimeInterval', blank=True, null=True)  # Field name made lowercase.
    samplingtimespace = models.BigIntegerField(db_column='samplingTimeSpace', blank=True, null=True)  # Field name made lowercase.
    samplingsize = models.BigIntegerField(db_column='samplingSize', blank=True, null=True)  # Field name made lowercase.
    samplingpopulation = models.BigIntegerField(db_column='samplingPopulation', blank=True, null=True)  # Field name made lowercase.
    samplingprobability = models.FloatField(db_column='samplingProbability', blank=True, null=True)  # Field name made lowercase.
    datalinkframesize = models.IntegerField(db_column='dataLinkFrameSize', blank=True, null=True)  # Field name made lowercase.
    ipheaderpacketsection = models.TextField(db_column='ipHeaderPacketSection', blank=True, null=True)  # Field name made lowercase.
    ippayloadpacketsection = models.TextField(db_column='ipPayloadPacketSection', blank=True, null=True)  # Field name made lowercase.
    datalinkframesection = models.TextField(db_column='dataLinkFrameSection', blank=True, null=True)  # Field name made lowercase.
    mplslabelstacksection = models.TextField(db_column='mplsLabelStackSection', blank=True, null=True)  # Field name made lowercase.
    mplspayloadpacketsection = models.TextField(db_column='mplsPayloadPacketSection', blank=True, null=True)  # Field name made lowercase.
    selectoridtotalpktsobserved = models.BigIntegerField(db_column='selectorIdTotalPktsObserved', blank=True, null=True)  # Field name made lowercase.
    selectoridtotalpktsselected = models.BigIntegerField(db_column='selectorIdTotalPktsSelected', blank=True, null=True)  # Field name made lowercase.
    absoluteerror = models.FloatField(db_column='absoluteError', blank=True, null=True)  # Field name made lowercase.
    relativeerror = models.FloatField(db_column='relativeError', blank=True, null=True)  # Field name made lowercase.
    observationtimeseconds = models.BigIntegerField(db_column='observationTimeSeconds', blank=True, null=True)  # Field name made lowercase.
    observationtimemilliseconds = models.BigIntegerField(db_column='observationTimeMilliseconds', blank=True, null=True)  # Field name made lowercase.
    observationtimemicroseconds = models.BigIntegerField(db_column='observationTimeMicroseconds', blank=True, null=True)  # Field name made lowercase.
    observationtimenanoseconds = models.BigIntegerField(db_column='observationTimeNanoseconds', blank=True, null=True)  # Field name made lowercase.
    digesthashvalue = models.BigIntegerField(db_column='digestHashValue', blank=True, null=True)  # Field name made lowercase.
    hashippayloadoffset = models.BigIntegerField(db_column='hashIPPayloadOffset', blank=True, null=True)  # Field name made lowercase.
    hashippayloadsize = models.BigIntegerField(db_column='hashIPPayloadSize', blank=True, null=True)  # Field name made lowercase.
    hashoutputrangemin = models.BigIntegerField(db_column='hashOutputRangeMin', blank=True, null=True)  # Field name made lowercase.
    hashoutputrangemax = models.BigIntegerField(db_column='hashOutputRangeMax', blank=True, null=True)  # Field name made lowercase.
    hashselectedrangemin = models.BigIntegerField(db_column='hashSelectedRangeMin', blank=True, null=True)  # Field name made lowercase.
    hashselectedrangemax = models.BigIntegerField(db_column='hashSelectedRangeMax', blank=True, null=True)  # Field name made lowercase.
    hashdigestoutput = models.BooleanField(db_column='hashDigestOutput', blank=True, null=True)  # Field name made lowercase.
    hashinitialiservalue = models.BigIntegerField(db_column='hashInitialiserValue', blank=True, null=True)  # Field name made lowercase.
    selectorname = models.TextField(db_column='selectorName', blank=True, null=True)  # Field name made lowercase.
    uppercilimit = models.FloatField(db_column='upperCILimit', blank=True, null=True)  # Field name made lowercase.
    lowercilimit = models.FloatField(db_column='lowerCILimit', blank=True, null=True)  # Field name made lowercase.
    confidencelevel = models.FloatField(db_column='confidenceLevel', blank=True, null=True)  # Field name made lowercase.
    informationelementdatatype = models.SmallIntegerField(db_column='informationElementDataType', blank=True, null=True)  # Field name made lowercase.
    informationelementdescription = models.TextField(db_column='informationElementDescription', blank=True, null=True)  # Field name made lowercase.
    informationelementname = models.TextField(db_column='informationElementName', blank=True, null=True)  # Field name made lowercase.
    informationelementrangebegin = models.BigIntegerField(db_column='informationElementRangeBegin', blank=True, null=True)  # Field name made lowercase.
    informationelementrangeend = models.BigIntegerField(db_column='informationElementRangeEnd', blank=True, null=True)  # Field name made lowercase.
    informationelementsemantics = models.SmallIntegerField(db_column='informationElementSemantics', blank=True, null=True)  # Field name made lowercase.
    informationelementunits = models.IntegerField(db_column='informationElementUnits', blank=True, null=True)  # Field name made lowercase.
    privateenterprisenumber = models.BigIntegerField(db_column='privateEnterpriseNumber', blank=True, null=True)  # Field name made lowercase.
    virtualstationinterfaceid = models.TextField(db_column='virtualStationInterfaceId', blank=True, null=True)  # Field name made lowercase.
    virtualstationinterfacename = models.TextField(db_column='virtualStationInterfaceName', blank=True, null=True)  # Field name made lowercase.
    virtualstationuuid = models.TextField(db_column='virtualStationUUID', blank=True, null=True)  # Field name made lowercase.
    virtualstationname = models.TextField(db_column='virtualStationName', blank=True, null=True)  # Field name made lowercase.
    layer2segmentid = models.BigIntegerField(db_column='layer2SegmentId', blank=True, null=True)  # Field name made lowercase.
    layer2octetdeltacount = models.BigIntegerField(db_column='layer2OctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    layer2octettotalcount = models.BigIntegerField(db_column='layer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    ingressunicastpackettotalcount = models.BigIntegerField(db_column='ingressUnicastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    ingressmulticastpackettotalcount = models.BigIntegerField(db_column='ingressMulticastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    ingressbroadcastpackettotalcount = models.BigIntegerField(db_column='ingressBroadcastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    egressunicastpackettotalcount = models.BigIntegerField(db_column='egressUnicastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    egressbroadcastpackettotalcount = models.BigIntegerField(db_column='egressBroadcastPacketTotalCount', blank=True, null=True)  # Field name made lowercase.
    monitoringintervalstartmilliseconds = models.BigIntegerField(db_column='monitoringIntervalStartMilliSeconds', blank=True, null=True)  # Field name made lowercase.
    monitoringintervalendmilliseconds = models.BigIntegerField(db_column='monitoringIntervalEndMilliSeconds', blank=True, null=True)  # Field name made lowercase.
    portrangestart = models.IntegerField(db_column='portRangeStart', blank=True, null=True)  # Field name made lowercase.
    portrangeend = models.IntegerField(db_column='portRangeEnd', blank=True, null=True)  # Field name made lowercase.
    portrangestepsize = models.IntegerField(db_column='portRangeStepSize', blank=True, null=True)  # Field name made lowercase.
    portrangenumports = models.IntegerField(db_column='portRangeNumPorts', blank=True, null=True)  # Field name made lowercase.
    stamacaddress = models.TextField(db_column='staMacAddress', blank=True, null=True)  # Field name made lowercase.
    staipv4address = models.GenericIPAddressField(db_column='staIPv4Address', blank=True, null=True)  # Field name made lowercase.
    wtpmacaddress = models.TextField(db_column='wtpMacAddress', blank=True, null=True)  # Field name made lowercase.
    ingressinterfacetype = models.BigIntegerField(db_column='ingressInterfaceType', blank=True, null=True)  # Field name made lowercase.
    egressinterfacetype = models.BigIntegerField(db_column='egressInterfaceType', blank=True, null=True)  # Field name made lowercase.
    rtpsequencenumber = models.IntegerField(db_column='rtpSequenceNumber', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='userName', blank=True, null=True)  # Field name made lowercase.
    applicationcategoryname = models.TextField(db_column='applicationCategoryName', blank=True, null=True)  # Field name made lowercase.
    applicationsubcategoryname = models.TextField(db_column='applicationSubCategoryName', blank=True, null=True)  # Field name made lowercase.
    applicationgroupname = models.TextField(db_column='applicationGroupName', blank=True, null=True)  # Field name made lowercase.
    originalflowspresent = models.BigIntegerField(db_column='originalFlowsPresent', blank=True, null=True)  # Field name made lowercase.
    originalflowsinitiated = models.BigIntegerField(db_column='originalFlowsInitiated', blank=True, null=True)  # Field name made lowercase.
    originalflowscompleted = models.BigIntegerField(db_column='originalFlowsCompleted', blank=True, null=True)  # Field name made lowercase.
    distinctcountofsourceipaddress = models.BigIntegerField(db_column='distinctCountOfSourceIPAddress', blank=True, null=True)  # Field name made lowercase.
    distinctcountofdestinationipaddress = models.BigIntegerField(db_column='distinctCountOfDestinationIPAddress', blank=True, null=True)  # Field name made lowercase.
    distinctcountofsourceipv4address = models.BigIntegerField(db_column='distinctCountOfSourceIPv4Address', blank=True, null=True)  # Field name made lowercase.
    distinctcountofdestinationipv4address = models.BigIntegerField(db_column='distinctCountOfDestinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    distinctcountofsourceipv6address = models.BigIntegerField(db_column='distinctCountOfSourceIPv6Address', blank=True, null=True)  # Field name made lowercase.
    distinctcountofdestinationipv6address = models.BigIntegerField(db_column='distinctCountOfDestinationIPv6Address', blank=True, null=True)  # Field name made lowercase.
    valuedistributionmethod = models.SmallIntegerField(db_column='valueDistributionMethod', blank=True, null=True)  # Field name made lowercase.
    rfc3550jittermilliseconds = models.BigIntegerField(db_column='rfc3550JitterMilliseconds', blank=True, null=True)  # Field name made lowercase.
    rfc3550jittermicroseconds = models.BigIntegerField(db_column='rfc3550JitterMicroseconds', blank=True, null=True)  # Field name made lowercase.
    rfc3550jitternanoseconds = models.BigIntegerField(db_column='rfc3550JitterNanoseconds', blank=True, null=True)  # Field name made lowercase.
    dot1qdei = models.BooleanField(db_column='dot1qDEI', blank=True, null=True)  # Field name made lowercase.
    dot1qcustomerdei = models.BooleanField(db_column='dot1qCustomerDEI', blank=True, null=True)  # Field name made lowercase.
    flowselectoralgorithm = models.IntegerField(db_column='flowSelectorAlgorithm', blank=True, null=True)  # Field name made lowercase.
    flowselectedoctetdeltacount = models.BigIntegerField(db_column='flowSelectedOctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    flowselectedpacketdeltacount = models.BigIntegerField(db_column='flowSelectedPacketDeltaCount', blank=True, null=True)  # Field name made lowercase.
    flowselectedflowdeltacount = models.BigIntegerField(db_column='flowSelectedFlowDeltaCount', blank=True, null=True)  # Field name made lowercase.
    selectoridtotalflowsobserved = models.BigIntegerField(db_column='selectorIDTotalFlowsObserved', blank=True, null=True)  # Field name made lowercase.
    selectoridtotalflowsselected = models.BigIntegerField(db_column='selectorIDTotalFlowsSelected', blank=True, null=True)  # Field name made lowercase.
    samplingflowinterval = models.BigIntegerField(db_column='samplingFlowInterval', blank=True, null=True)  # Field name made lowercase.
    samplingflowspacing = models.BigIntegerField(db_column='samplingFlowSpacing', blank=True, null=True)  # Field name made lowercase.
    flowsamplingtimeinterval = models.BigIntegerField(db_column='flowSamplingTimeInterval', blank=True, null=True)  # Field name made lowercase.
    flowsamplingtimespacing = models.BigIntegerField(db_column='flowSamplingTimeSpacing', blank=True, null=True)  # Field name made lowercase.
    hashflowdomain = models.IntegerField(db_column='hashFlowDomain', blank=True, null=True)  # Field name made lowercase.
    transportoctetdeltacount = models.BigIntegerField(db_column='transportOctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    transportpacketdeltacount = models.BigIntegerField(db_column='transportPacketDeltaCount', blank=True, null=True)  # Field name made lowercase.
    originalexporteripv4address = models.GenericIPAddressField(db_column='originalExporterIPv4Address', blank=True, null=True)  # Field name made lowercase.
    originalexporteripv6address = models.GenericIPAddressField(db_column='originalExporterIPv6Address', blank=True, null=True)  # Field name made lowercase.
    originalobservationdomainid = models.BigIntegerField(db_column='originalObservationDomainId', blank=True, null=True)  # Field name made lowercase.
    intermediateprocessid = models.BigIntegerField(db_column='intermediateProcessId', blank=True, null=True)  # Field name made lowercase.
    ignoreddatarecordtotalcount = models.BigIntegerField(db_column='ignoredDataRecordTotalCount', blank=True, null=True)  # Field name made lowercase.
    datalinkframetype = models.IntegerField(db_column='dataLinkFrameType', blank=True, null=True)  # Field name made lowercase.
    sectionoffset = models.IntegerField(db_column='sectionOffset', blank=True, null=True)  # Field name made lowercase.
    sectionexportedoctets = models.IntegerField(db_column='sectionExportedOctets', blank=True, null=True)  # Field name made lowercase.
    dot1qserviceinstancetag = models.TextField(db_column='dot1qServiceInstanceTag', blank=True, null=True)  # Field name made lowercase.
    dot1qserviceinstanceid = models.BigIntegerField(db_column='dot1qServiceInstanceId', blank=True, null=True)  # Field name made lowercase.
    dot1qserviceinstancepriority = models.SmallIntegerField(db_column='dot1qServiceInstancePriority', blank=True, null=True)  # Field name made lowercase.
    dot1qcustomersourcemacaddress = models.TextField(db_column='dot1qCustomerSourceMacAddress', blank=True, null=True)  # Field name made lowercase.
    dot1qcustomerdestinationmacaddress = models.TextField(db_column='dot1qCustomerDestinationMacAddress', blank=True, null=True)  # Field name made lowercase.
    postlayer2octetdeltacount = models.BigIntegerField(db_column='postLayer2OctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    postmcastlayer2octetdeltacount = models.BigIntegerField(db_column='postMCastLayer2OctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    postlayer2octettotalcount = models.BigIntegerField(db_column='postLayer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    postmcastlayer2octettotalcount = models.BigIntegerField(db_column='postMCastLayer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    minimumlayer2totallength = models.BigIntegerField(db_column='minimumLayer2TotalLength', blank=True, null=True)  # Field name made lowercase.
    maximumlayer2totallength = models.BigIntegerField(db_column='maximumLayer2TotalLength', blank=True, null=True)  # Field name made lowercase.
    droppedlayer2octetdeltacount = models.BigIntegerField(db_column='droppedLayer2OctetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    droppedlayer2octettotalcount = models.BigIntegerField(db_column='droppedLayer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    ignoredlayer2octettotalcount = models.BigIntegerField(db_column='ignoredLayer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    notsentlayer2octettotalcount = models.BigIntegerField(db_column='notSentLayer2OctetTotalCount', blank=True, null=True)  # Field name made lowercase.
    layer2octetdeltasumofsquares = models.BigIntegerField(db_column='layer2OctetDeltaSumOfSquares', blank=True, null=True)  # Field name made lowercase.
    layer2octettotalsumofsquares = models.BigIntegerField(db_column='layer2OctetTotalSumOfSquares', blank=True, null=True)  # Field name made lowercase.
    layer2framedeltacount = models.BigIntegerField(db_column='layer2FrameDeltaCount', blank=True, null=True)  # Field name made lowercase.
    layer2frametotalcount = models.BigIntegerField(db_column='layer2FrameTotalCount', blank=True, null=True)  # Field name made lowercase.
    pseudowiredestinationipv4address = models.GenericIPAddressField(db_column='pseudoWireDestinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    ignoredlayer2frametotalcount = models.BigIntegerField(db_column='ignoredLayer2FrameTotalCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flows'


class FlowsFIpv4IpTotals(models.Model):
    ipv4address = models.GenericIPAddressField(db_column='ipv4Address', primary_key=True)  # Field name made lowercase.
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flows_f_ipv4_ip_totals'
        unique_together = (('ipv4address', 'count'),)


class FlowsFIpv4Min(models.Model):
    id = models.BigIntegerField(primary_key=True)
    flowstartmilliseconds = models.BigIntegerField(db_column='flowStartMilliseconds', blank=True, null=True)  # Field name made lowercase.
    duration = models.BigIntegerField(blank=True, null=True)
    sourceipv4address = models.GenericIPAddressField(db_column='sourceIPv4Address', blank=True, null=True)  # Field name made lowercase.
    destinationipv4address = models.GenericIPAddressField(db_column='destinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    octetdeltacount = models.BigIntegerField(db_column='octetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    protocolidentifier = models.SmallIntegerField(db_column='protocolIdentifier', blank=True, null=True)  # Field name made lowercase.
    sourcetransportport = models.IntegerField(db_column='sourceTransportPort', blank=True, null=True)  # Field name made lowercase.
    destinationtransportport = models.IntegerField(db_column='destinationTransportPort', blank=True, null=True)  # Field name made lowercase.
    ingressinterface = models.BigIntegerField(db_column='ingressInterface', blank=True, null=True)  # Field name made lowercase.
    egressinterface = models.BigIntegerField(db_column='egressInterface', blank=True, null=True)  # Field name made lowercase.
    ipversion = models.SmallIntegerField(db_column='ipVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flows_f_ipv4_min'


class FlowsFIpv4Subset(models.Model):
    id = models.BigIntegerField(primary_key=True)
    flowstartmilliseconds = models.BigIntegerField(db_column='flowStartMilliseconds', blank=True, null=True)  # Field name made lowercase.
    flowendmilliseconds = models.BigIntegerField(db_column='flowEndMilliseconds', blank=True, null=True)  # Field name made lowercase.
    sourceipv4address = models.GenericIPAddressField(db_column='sourceIPv4Address', blank=True, null=True)  # Field name made lowercase.
    destinationipv4address = models.GenericIPAddressField(db_column='destinationIPv4Address', blank=True, null=True)  # Field name made lowercase.
    octetdeltacount = models.BigIntegerField(db_column='octetDeltaCount', blank=True, null=True)  # Field name made lowercase.
    protocolidentifier = models.SmallIntegerField(db_column='protocolIdentifier', blank=True, null=True)  # Field name made lowercase.
    sourcetransportport = models.IntegerField(db_column='sourceTransportPort', blank=True, null=True)  # Field name made lowercase.
    destinationtransportport = models.IntegerField(db_column='destinationTransportPort', blank=True, null=True)  # Field name made lowercase.
    ingressinterface = models.BigIntegerField(db_column='ingressInterface', blank=True, null=True)  # Field name made lowercase.
    egressinterface = models.BigIntegerField(db_column='egressInterface', blank=True, null=True)  # Field name made lowercase.
    ipversion = models.SmallIntegerField(db_column='ipVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flows_f_ipv4_subset'


class FlowsFIpv4Totals(models.Model):
    sourceipv4address = models.GenericIPAddressField(db_column='sourceIPv4Address', primary_key=True)  # Field name made lowercase.
    destinationipv4address = models.GenericIPAddressField(db_column='destinationIPv4Address')  # Field name made lowercase.
    totalbytes = models.DecimalField(db_column='totalBytes', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flows_f_ipv4_totals'
        unique_together = (('sourceipv4address', 'destinationipv4address'),)


class FlowsFProtocolCounts(models.Model):
    protocolidentifier = models.SmallIntegerField(db_column='protocolIdentifier', primary_key=True)  # Field name made lowercase.
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'flows_f_protocol_counts'
        unique_together = (('protocolidentifier', 'count'),)


class FlowsFUniqueIpv4(models.Model):
    ipv4address = models.GenericIPAddressField(db_column='ipv4Address', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flows_f_unique_ipv4'
