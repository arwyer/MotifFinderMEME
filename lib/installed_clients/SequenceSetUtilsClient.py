# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class SequenceSetUtils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='dev',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def SSFromLocations(self, params, context=None):
        """
        :param params: instance of type "LocationInputParams"
           (LocationInputParams, direct inputs for buildFromLocation:
           required: genome_ref - genome referenced by sequence locations
           genlocations - list of sequence locations sepecified by a location
           ids optional: seqsetname - name of sequence set output object) ->
           structure: parameter "ws_name" of type "workspace_name" (workspace
           name of the object), parameter "seqlocations" of list of type
           "sequence_location" (sequence_location, sequence location
           container for seperation by genome: genome_ref - genome referenced
           by sequence locations genlocations - list of sequence locations
           sepecified by a location ids) -> structure: parameter "genome_ref"
           of type "GenomeRef" (Ref to a genome @id ws KBaseGenomes.Genome),
           parameter "locations" of list of type "location_id" (Input
           parameters for buildFromLocations location_id, relevent
           identifiers to identify a sequence location: contig_id - string -
           name relevent to the assembly contig, e.g. chr1, chrX, contig1,
           etc. start - int - start of sequence end - int - end of sequence
           orientation - range("-", "+") - reference to the sense of a
           DNA/RNA strand) -> structure: parameter "contig_id" of String,
           parameter "start" of Long, parameter "sense" of type "orientation"
           (DNA/RNA strand orientation @range("-", "+")), parameter "end" of
           Long, parameter "seqsetname" of String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
        """
        return self._client.run_job('SequenceSetUtils.SSFromLocations',
                                    [params], self._service_ver, context)

    def buildFromFasta(self, params, context=None):
        """
        :param params: instance of type "FastaInputParams" (Input parameters
           for buildFromFasta: required: ws_name - workspace name file -
           identifiers for fasta file optional: seqsetname - name of sequence
           set output object) -> structure: parameter "ws_name" of type
           "workspace_name" (workspace name of the object), parameter "file"
           of type "File" -> structure: parameter "path" of String, parameter
           "shock_id" of String, parameter "ftp_url" of String, parameter
           "seqsetname" of String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
        """
        return self._client.run_job('SequenceSetUtils.buildFromFasta',
                                    [params], self._service_ver, context)

    def SeqSetToFasta(self, params, context=None):
        """
        :param params: instance of type "SeqSet2FastaInput" -> structure:
           parameter "ws_name" of type "workspace_name" (workspace name of
           the object), parameter "SS_ref" of type "SequenceSetRef" (Ref to a
           sequence set @id ws KBaseGeneRegulation.SequenceSet)
        :returns: instance of type "SS2FastaOutputParams" -> structure:
           parameter "fasta_output" of type "File" -> structure: parameter
           "path" of String, parameter "shock_id" of String, parameter
           "ftp_url" of String
        """
        return self._client.run_job('SequenceSetUtils.SeqSetToFasta',
                                    [params], self._service_ver, context)

    def buildFromFeaturePromoters(self, params, context=None):
        """
        :param params: instance of type "FeatureSetInputParams" (Input
           parameters for buildFromFeatureSet required: ws_name - workspace
           name FeatureSet_ref - validated reference to feature set
           genome_ref - validated reference to genome upstream_length -
           length of region upstream of features to extract sequences from
           optional: seqsetname - name of sequence set output object) ->
           structure: parameter "ws_name" of type "workspace_name" (workspace
           name of the object), parameter "FeatureSet_ref" of type
           "FeatureSetRef" (Ref to a feature set @id ws
           KBaseCollections.FeatureSet), parameter "genome_ref" of type
           "GenomeRef" (Ref to a genome @id ws KBaseGenomes.Genome),
           parameter "upstream_length" of Long, parameter "seqsetname" of
           String
        :returns: instance of type "SequenceSetOutputParams" (SequenceSet_ref
           - KBase object reference to sequence set) -> structure: parameter
           "SequenceSet_ref" of type "SequenceSetRef" (Ref to a sequence set
           @id ws KBaseGeneRegulation.SequenceSet)
        """
        return self._client.run_job('SequenceSetUtils.buildFromFeaturePromoters',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('SequenceSetUtils.status',
                                    [], self._service_ver, context)
