import responses
import pytest

from pycheckpoint_api.firewallManagement.exception import MandatoryFieldMissing


@responses.activate
def test_add_service_dce_rpc(firewallManagement, resp_service_dce_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/add-service-dce-rpc",
        json=resp_service_dce_rpc,
        status=200,
    )

    resp = firewallManagement.service_applications.service_dce_rpc.add(
        name="New_DCE-RPC_Service_1",
        interface_uuid="97aeb460-9aea-11d5-bd16-0090272ccb30",
        keep_connections_open_after_policy_installation=False,
    )

    assert resp.uid == "b02db15d-c8e9-408c-a789-095b6d76db02"
    assert resp.name == "New_DCE-RPC_Service_1"


@responses.activate
def test_show_service_dce_rpc(firewallManagement, resp_service_dce_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-service-dce-rpc",
        json=resp_service_dce_rpc,
        status=200,
    )

    resp = firewallManagement.service_applications.service_dce_rpc.show(
        uid="b02db15d-c8e9-408c-a789-095b6d76db02"
    )

    assert resp.uid == "b02db15d-c8e9-408c-a789-095b6d76db02"
    assert resp.name == "New_DCE-RPC_Service_1"


@responses.activate
def test_set_service_dce_rpc(firewallManagement, resp_service_dce_rpc):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/set-service-dce-rpc",
        json=resp_service_dce_rpc,
        status=200,
    )

    resp = firewallManagement.service_applications.service_dce_rpc.set(
        uid="b02db15d-c8e9-408c-a789-095b6d76db02",
        new_name="New_DCE-RPC_Service_1",
        interface_uuid="97aeb460-9aea-11d5-bd16-0090272ccb30",
        keep_connections_open_after_policy_installation=False,
    )

    assert resp.uid == "b02db15d-c8e9-408c-a789-095b6d76db02"
    assert resp.name == "New_DCE-RPC_Service_1"

    resp = firewallManagement.service_applications.service_dce_rpc.set(
        name="New_DCE-RPC_Service_1",
        interface_uuid="97aeb460-9aea-11d5-bd16-0090272ccb30",
    )

    assert resp.uid == "b02db15d-c8e9-408c-a789-095b6d76db02"
    assert resp.name == "New_DCE-RPC_Service_1"

    # None arguments
    with pytest.raises(MandatoryFieldMissing):
        firewallManagement.service_applications.service_dce_rpc.set()


@responses.activate
def test_delete_service_dce_rpc(firewallManagement, resp_message_ok):

    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/delete-service-dce-rpc",
        json=resp_message_ok,
        status=200,
    )

    resp = firewallManagement.service_applications.service_dce_rpc.delete(
        uid="b02db15d-c8e9-408c-a789-095b6d76db02"
    )

    assert resp.message == "OK"


@responses.activate
def test_show_services_dce_rpc(firewallManagement, resp_from_to_objects):
    responses.add(
        responses.POST,
        url="https://127.0.0.1:443/web_api/v1.5/show-services-dce-rpc",
        json=resp_from_to_objects,
        status=200,
    )

    resp = (
        firewallManagement.service_applications.service_dce_rpc.show_services_dce_rpc()
    )

    assert isinstance(resp.total, int)