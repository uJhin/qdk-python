# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class BlobDetails(msrest.serialization.Model):
    """Blob details.

    All required parameters must be populated in order to send to Azure.

    :ivar container_name: Required. The container name.
    :vartype container_name: str
    :ivar blob_name: The blob name.
    :vartype blob_name: str
    """

    _validation = {
        'container_name': {'required': True},
    }

    _attribute_map = {
        'container_name': {'key': 'containerName', 'type': 'str'},
        'blob_name': {'key': 'blobName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword container_name: Required. The container name.
        :paramtype container_name: str
        :keyword blob_name: The blob name.
        :paramtype blob_name: str
        """
        super(BlobDetails, self).__init__(**kwargs)
        self.container_name = kwargs['container_name']
        self.blob_name = kwargs.get('blob_name', None)


class CostEstimate(msrest.serialization.Model):
    """The job cost billed by the provider. The final cost on your bill might be slightly different due to added taxes and currency conversion rates.

    :ivar currency_code: The currency code.
    :vartype currency_code: str
    :ivar events: List of usage events.
    :vartype events: list[~azure.quantum._client.models.UsageEvent]
    :ivar estimated_total: The estimated total.
    :vartype estimated_total: float
    """

    _attribute_map = {
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'events': {'key': 'events', 'type': '[UsageEvent]'},
        'estimated_total': {'key': 'estimatedTotal', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword currency_code: The currency code.
        :paramtype currency_code: str
        :keyword events: List of usage events.
        :paramtype events: list[~azure.quantum._client.models.UsageEvent]
        :keyword estimated_total: The estimated total.
        :paramtype estimated_total: float
        """
        super(CostEstimate, self).__init__(**kwargs)
        self.currency_code = kwargs.get('currency_code', None)
        self.events = kwargs.get('events', None)
        self.estimated_total = kwargs.get('estimated_total', None)


class ErrorData(msrest.serialization.Model):
    """An error response from Azure.

    :ivar code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for displaying in a user
     interface.
    :vartype message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code: An identifier for the error. Codes are invariant and are intended to be consumed
         programmatically.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for displaying in a
         user interface.
        :paramtype message: str
        """
        super(ErrorData, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class JobDetails(msrest.serialization.Model):
    """Job details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The job id.
    :vartype id: str
    :ivar name: The job name. Is not required for the name to be unique and it's only used for
     display purposes.
    :vartype name: str
    :ivar container_uri: Required. The blob container SAS uri, the container is used to host job
     data.
    :vartype container_uri: str
    :ivar input_data_uri: The input blob SAS uri, if specified, it will override the default input
     blob in the container.
    :vartype input_data_uri: str
    :ivar input_data_format: Required. The format of the input data.
    :vartype input_data_format: str
    :ivar input_params: The input parameters for the job. JSON object used by the target solver. It
     is expected that the size of this object is small and only used to specify parameters for the
     execution target, not the input data.
    :vartype input_params: any
    :ivar provider_id: Required. The unique identifier for the provider.
    :vartype provider_id: str
    :ivar target: Required. The target identifier to run the job.
    :vartype target: str
    :ivar metadata: The job metadata. Metadata provides client the ability to store client-specific
     information.
    :vartype metadata: dict[str, str]
    :ivar output_data_uri: The output blob SAS uri. When a job finishes successfully, results will
     be uploaded to this blob.
    :vartype output_data_uri: str
    :ivar output_data_format: The format of the output data.
    :vartype output_data_format: str
    :ivar status: The job status. Possible values include: "Waiting", "Executing", "Succeeded",
     "Failed", "Cancelled".
    :vartype status: str or ~azure.quantum._client.models.JobStatus
    :ivar creation_time: The creation time of the job.
    :vartype creation_time: ~datetime.datetime
    :ivar begin_execution_time: The time when the job began execution.
    :vartype begin_execution_time: ~datetime.datetime
    :ivar end_execution_time: The time when the job finished execution.
    :vartype end_execution_time: ~datetime.datetime
    :ivar cancellation_time: The time when a job was successfully cancelled.
    :vartype cancellation_time: ~datetime.datetime
    :ivar cost_estimate: The job cost billed by the provider. The final cost on your bill might be
     slightly different due to added taxes and currency conversion rates.
    :vartype cost_estimate: ~azure.quantum._client.models.CostEstimate
    :ivar error_data: The error data for the job. This is expected only when Status 'Failed'.
    :vartype error_data: ~azure.quantum._client.models.ErrorData
    :ivar tags: A set of tags. List of user-supplied tags associated with the job.
    :vartype tags: list[str]
    """

    _validation = {
        'container_uri': {'required': True},
        'input_data_format': {'required': True},
        'provider_id': {'required': True},
        'target': {'required': True},
        'status': {'readonly': True},
        'creation_time': {'readonly': True},
        'begin_execution_time': {'readonly': True},
        'end_execution_time': {'readonly': True},
        'cancellation_time': {'readonly': True},
        'cost_estimate': {'readonly': True},
        'error_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'container_uri': {'key': 'containerUri', 'type': 'str'},
        'input_data_uri': {'key': 'inputDataUri', 'type': 'str'},
        'input_data_format': {'key': 'inputDataFormat', 'type': 'str'},
        'input_params': {'key': 'inputParams', 'type': 'object'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
        'output_data_uri': {'key': 'outputDataUri', 'type': 'str'},
        'output_data_format': {'key': 'outputDataFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'begin_execution_time': {'key': 'beginExecutionTime', 'type': 'iso-8601'},
        'end_execution_time': {'key': 'endExecutionTime', 'type': 'iso-8601'},
        'cancellation_time': {'key': 'cancellationTime', 'type': 'iso-8601'},
        'cost_estimate': {'key': 'costEstimate', 'type': 'CostEstimate'},
        'error_data': {'key': 'errorData', 'type': 'ErrorData'},
        'tags': {'key': 'tags', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword id: The job id.
        :paramtype id: str
        :keyword name: The job name. Is not required for the name to be unique and it's only used for
         display purposes.
        :paramtype name: str
        :keyword container_uri: Required. The blob container SAS uri, the container is used to host job
         data.
        :paramtype container_uri: str
        :keyword input_data_uri: The input blob SAS uri, if specified, it will override the default
         input blob in the container.
        :paramtype input_data_uri: str
        :keyword input_data_format: Required. The format of the input data.
        :paramtype input_data_format: str
        :keyword input_params: The input parameters for the job. JSON object used by the target solver.
         It is expected that the size of this object is small and only used to specify parameters for
         the execution target, not the input data.
        :paramtype input_params: any
        :keyword provider_id: Required. The unique identifier for the provider.
        :paramtype provider_id: str
        :keyword target: Required. The target identifier to run the job.
        :paramtype target: str
        :keyword metadata: The job metadata. Metadata provides client the ability to store
         client-specific information.
        :paramtype metadata: dict[str, str]
        :keyword output_data_uri: The output blob SAS uri. When a job finishes successfully, results
         will be uploaded to this blob.
        :paramtype output_data_uri: str
        :keyword output_data_format: The format of the output data.
        :paramtype output_data_format: str
        :keyword tags: A set of tags. List of user-supplied tags associated with the job.
        :paramtype tags: list[str]
        """
        super(JobDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.container_uri = kwargs['container_uri']
        self.input_data_uri = kwargs.get('input_data_uri', None)
        self.input_data_format = kwargs['input_data_format']
        self.input_params = kwargs.get('input_params', None)
        self.provider_id = kwargs['provider_id']
        self.target = kwargs['target']
        self.metadata = kwargs.get('metadata', None)
        self.output_data_uri = kwargs.get('output_data_uri', None)
        self.output_data_format = kwargs.get('output_data_format', None)
        self.status = None
        self.creation_time = None
        self.begin_execution_time = None
        self.end_execution_time = None
        self.cancellation_time = None
        self.cost_estimate = None
        self.error_data = None
        self.tags = kwargs.get('tags', None)


class JobDetailsList(msrest.serialization.Model):
    """List of job details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum._client.models.JobDetails]
    :ivar count: Total records count number.
    :vartype count: long
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[JobDetails]'},
        'count': {'key': 'count', 'type': 'long'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword count: Total records count number.
        :paramtype count: long
        """
        super(JobDetailsList, self).__init__(**kwargs)
        self.value = None
        self.count = kwargs.get('count', None)
        self.next_link = None


class JsonPatchDocument(msrest.serialization.Model):
    """A JSONPatch document as defined by RFC 6902.

    All required parameters must be populated in order to send to Azure.

    :ivar op: Required. The operation to be performed. Possible values include: "add", "remove",
     "replace", "move", "copy", "test".
    :vartype op: str or ~azure.quantum._client.models.JsonPatchOperation
    :ivar path: Required. A JSON-Pointer.
    :vartype path: str
    :ivar value: A value to be used in the operation on the path.
    :vartype value: any
    :ivar from_property: Optional field used in copy and move operations.
    :vartype from_property: str
    """

    _validation = {
        'op': {'required': True},
        'path': {'required': True},
    }

    _attribute_map = {
        'op': {'key': 'op', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'from_property': {'key': 'from', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword op: Required. The operation to be performed. Possible values include: "add", "remove",
         "replace", "move", "copy", "test".
        :paramtype op: str or ~azure.quantum._client.models.JsonPatchOperation
        :keyword path: Required. A JSON-Pointer.
        :paramtype path: str
        :keyword value: A value to be used in the operation on the path.
        :paramtype value: any
        :keyword from_property: Optional field used in copy and move operations.
        :paramtype from_property: str
        """
        super(JsonPatchDocument, self).__init__(**kwargs)
        self.op = kwargs['op']
        self.path = kwargs['path']
        self.value = kwargs.get('value', None)
        self.from_property = kwargs.get('from_property', None)


class ProviderStatus(msrest.serialization.Model):
    """Providers status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Provider id.
    :vartype id: str
    :ivar current_availability: Provider availability. Possible values include: "Available",
     "Degraded", "Unavailable".
    :vartype current_availability: str or ~azure.quantum._client.models.ProviderAvailability
    :ivar targets:
    :vartype targets: list[~azure.quantum._client.models.TargetStatus]
    """

    _validation = {
        'id': {'readonly': True},
        'current_availability': {'readonly': True},
        'targets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_availability': {'key': 'currentAvailability', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[TargetStatus]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ProviderStatus, self).__init__(**kwargs)
        self.id = None
        self.current_availability = None
        self.targets = None


class ProviderStatusList(msrest.serialization.Model):
    """Providers status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum._client.models.ProviderStatus]
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ProviderStatus]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ProviderStatusList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class Quota(msrest.serialization.Model):
    """Quota information.

    :ivar dimension: The name of the dimension associated with the quota.
    :vartype dimension: str
    :ivar scope: The scope at which the quota is applied. Possible values include: "Workspace",
     "Subscription".
    :vartype scope: str or ~azure.quantum._client.models.DimensionScope
    :ivar provider_id: The unique identifier for the provider.
    :vartype provider_id: str
    :ivar utilization: The amount of the usage that has been applied for the current period.
    :vartype utilization: float
    :ivar holds: The amount of the usage that has been reserved but not applied for the current
     period.
    :vartype holds: float
    :ivar limit: The maximum amount of usage allowed for the current period.
    :vartype limit: float
    :ivar period: The time period in which the quota's underlying meter is accumulated. Based on
     calendar year. 'None' is used for concurrent quotas. Possible values include: "None",
     "Monthly".
    :vartype period: str or ~azure.quantum._client.models.MeterPeriod
    """

    _attribute_map = {
        'dimension': {'key': 'dimension', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'utilization': {'key': 'utilization', 'type': 'float'},
        'holds': {'key': 'holds', 'type': 'float'},
        'limit': {'key': 'limit', 'type': 'float'},
        'period': {'key': 'period', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword dimension: The name of the dimension associated with the quota.
        :paramtype dimension: str
        :keyword scope: The scope at which the quota is applied. Possible values include: "Workspace",
         "Subscription".
        :paramtype scope: str or ~azure.quantum._client.models.DimensionScope
        :keyword provider_id: The unique identifier for the provider.
        :paramtype provider_id: str
        :keyword utilization: The amount of the usage that has been applied for the current period.
        :paramtype utilization: float
        :keyword holds: The amount of the usage that has been reserved but not applied for the current
         period.
        :paramtype holds: float
        :keyword limit: The maximum amount of usage allowed for the current period.
        :paramtype limit: float
        :keyword period: The time period in which the quota's underlying meter is accumulated. Based on
         calendar year. 'None' is used for concurrent quotas. Possible values include: "None",
         "Monthly".
        :paramtype period: str or ~azure.quantum._client.models.MeterPeriod
        """
        super(Quota, self).__init__(**kwargs)
        self.dimension = kwargs.get('dimension', None)
        self.scope = kwargs.get('scope', None)
        self.provider_id = kwargs.get('provider_id', None)
        self.utilization = kwargs.get('utilization', None)
        self.holds = kwargs.get('holds', None)
        self.limit = kwargs.get('limit', None)
        self.period = kwargs.get('period', None)


class QuotaList(msrest.serialization.Model):
    """List of quotas.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value:
    :vartype value: list[~azure.quantum._client.models.Quota]
    :ivar next_link: Link to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Quota]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(QuotaList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class RestError(msrest.serialization.Model):
    """Error information returned by the API.

    :ivar error: An error response from Azure.
    :vartype error: ~azure.quantum._client.models.ErrorData
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword error: An error response from Azure.
        :paramtype error: ~azure.quantum._client.models.ErrorData
        """
        super(RestError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class SasUriResponse(msrest.serialization.Model):
    """Get SAS URL operation response.

    :ivar sas_uri: A URL with a SAS token to upload a blob for execution in the given workspace.
    :vartype sas_uri: str
    """

    _attribute_map = {
        'sas_uri': {'key': 'sasUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword sas_uri: A URL with a SAS token to upload a blob for execution in the given workspace.
        :paramtype sas_uri: str
        """
        super(SasUriResponse, self).__init__(**kwargs)
        self.sas_uri = kwargs.get('sas_uri', None)


class TargetStatus(msrest.serialization.Model):
    """Target status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Target id.
    :vartype id: str
    :ivar current_availability: Target availability. Possible values include: "Available",
     "Degraded", "Unavailable".
    :vartype current_availability: str or ~azure.quantum._client.models.TargetAvailability
    :ivar average_queue_time: Average queue time in seconds.
    :vartype average_queue_time: long
    :ivar status_page: A page with detailed status of the provider.
    :vartype status_page: str
    """

    _validation = {
        'id': {'readonly': True},
        'current_availability': {'readonly': True},
        'average_queue_time': {'readonly': True},
        'status_page': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_availability': {'key': 'currentAvailability', 'type': 'str'},
        'average_queue_time': {'key': 'averageQueueTime', 'type': 'long'},
        'status_page': {'key': 'statusPage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(TargetStatus, self).__init__(**kwargs)
        self.id = None
        self.current_availability = None
        self.average_queue_time = None
        self.status_page = None


class UsageEvent(msrest.serialization.Model):
    """Usage event details.

    :ivar dimension_id: The dimension id.
    :vartype dimension_id: str
    :ivar dimension_name: The dimension name.
    :vartype dimension_name: str
    :ivar measure_unit: The unit of measure.
    :vartype measure_unit: str
    :ivar amount_billed: The amount billed.
    :vartype amount_billed: float
    :ivar amount_consumed: The amount consumed.
    :vartype amount_consumed: float
    :ivar unit_price: The unit price.
    :vartype unit_price: float
    """

    _attribute_map = {
        'dimension_id': {'key': 'dimensionId', 'type': 'str'},
        'dimension_name': {'key': 'dimensionName', 'type': 'str'},
        'measure_unit': {'key': 'measureUnit', 'type': 'str'},
        'amount_billed': {'key': 'amountBilled', 'type': 'float'},
        'amount_consumed': {'key': 'amountConsumed', 'type': 'float'},
        'unit_price': {'key': 'unitPrice', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword dimension_id: The dimension id.
        :paramtype dimension_id: str
        :keyword dimension_name: The dimension name.
        :paramtype dimension_name: str
        :keyword measure_unit: The unit of measure.
        :paramtype measure_unit: str
        :keyword amount_billed: The amount billed.
        :paramtype amount_billed: float
        :keyword amount_consumed: The amount consumed.
        :paramtype amount_consumed: float
        :keyword unit_price: The unit price.
        :paramtype unit_price: float
        """
        super(UsageEvent, self).__init__(**kwargs)
        self.dimension_id = kwargs.get('dimension_id', None)
        self.dimension_name = kwargs.get('dimension_name', None)
        self.measure_unit = kwargs.get('measure_unit', None)
        self.amount_billed = kwargs.get('amount_billed', None)
        self.amount_consumed = kwargs.get('amount_consumed', None)
        self.unit_price = kwargs.get('unit_price', None)
