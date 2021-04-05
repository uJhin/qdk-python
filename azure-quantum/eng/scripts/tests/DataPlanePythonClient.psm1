########################################################################################################
# Do NOT modify this section as it will get replaced by the base class defined in
# https://github.com/microsoft/azure-quantum-clients/blob/tests/common/DataPlaneBaseClient.psm1
# Start of "do NOT modify section"
########################################################################################################

class DataPlaneBaseClient
{
    DataPlaneBaseClient()
    {
        $type = $this.GetType()

        if ($type -eq [DataPlaneBaseClient])
        {
            throw("Class $type must be inherited")
        }
    }

    Prepare(
        [string]$PackageVersion
        ,[bool]$AllowPreRelease = $true)
    {
        throw("Must Override Method")        
    }

    SubmitQIOJob(
        [string]$SubscriptionId
        ,[string]$WorkspaceName
        ,[string]$JobId)
    {
        throw("Must Override Method")
    }
}

########################################################################################################
# End of "do NOT modify section"
########################################################################################################


class DataPlanePythonClient : DataPlaneBaseClient
{
    Prepare(
        [string]$PackageVersion
        ,[bool]$AllowPreRelease = $true)
    {
        $ProjectRoot = Join-Path $PSScriptRoot "../../../" -Resolve
        Push-Location $ProjectRoot
        try {
            # pip install azure_devtools pytest pytest-azurepipelines pytest-cov
            # conda env create -f environment.yml -n azure-quantum
            # conda activate azure-quantum

            if (![string]::IsNullOrEmpty($PackageVersion)){
                if ([string]::Equals("latest", $PackageVersion)) {
                    pip install azure-quantum | Write-Verbose
                    if ($LASTEXITCODE -ne 0) { throw "Error install local package" } 
                }
                else {
                    pip install azure-quantum $PackageVersion | Write-Verbose
                    if ($LASTEXITCODE -ne 0) { throw "Error install local package" } 
                }
            } 
            else {
                pip install -e . | Write-Verbose
                if ($LASTEXITCODE -ne 0) { throw "Error install local package" } 
            }
        }
        finally {
            Pop-Location
        }
    }

    SubmitQIOJob(
        [string]$SubscriptionId
        ,[string]$WorkspaceName
        ,[string]$JobId)
    {
        $env:AZURE_TEST_RUN_LIVE = "yes"
        Write-Verbose "Setting AZURE_TEST_RUN_LIVE to: $env:AZURE_TEST_RUN_LIVE"

        $env:QUANTUM_E2E_TESTS = "1"
        Write-Verbose "Setting QUANTUM_E2E_TESTS to: $env:QUANTUM_E2E_TESTS"

        Write-Verbose "Submitting job via DataPlane Python Client"
        Write-Verbose "  SubscriptionId: $SubscriptionId"
        Write-Verbose "  WorkspaceName: $WorkspaceName"

        $env:SUBSCRIPTION_ID = $SubscriptionId
        $env:QUANTUM_WORKSPACE_NAME = $WorkspaceName

        $TestProjectRoot = Join-Path $PSScriptRoot "../../../tests/" -Resolve

        Push-Location $TestProjectRoot
        try {
            Write-Verbose "Submiting job via DataPlane Python client..."
            pytest "./unit/test_job.py" -k "test_job_submit" | Write-Verbose
            if ($LASTEXITCODE -ne 0) { throw "At least one test has failed." } 
            Write-Verbose "  JobId: $JobId"
        }
        finally {
            Pop-Location
        }
    }
}
