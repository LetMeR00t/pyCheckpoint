from typing import List, Union

from box import Box

from pycheckpoint_api.models import Color
from pycheckpoint_api.utils import sanitize_secondary_parameters

from ..abstract.network_object import NetworkObject
from ..exception import MandatoryFieldMissing


class ApplicationSite(NetworkObject):
    def add(
        self,
        name: str,
        primary_category: str,
        url_list: Union[str, List[str]] = None,
        application_signature: Union[str, List[str]] = None,
        additional_categories: Union[str, List[str]] = None,
        description: str = None,
        tags: Union[str, List[str]] = None,
        urls_defined_as_regular_expression: bool = False,
        **kw,
    ) -> Box:
        """
        Create new object.

        Args:
            name (str): Object name. Must be unique in the domain.
            primary_category (str): Each application is assigned to one primary category based on its most defining aspect.
            url_list (Union[str, List[str]], optional): URLs that determine this particular application. Mandatory if
            application_signature is not set.
            application_signature (Union[str, List[str]], optional): Application signature generated by Signature Tool. \
            Mandatory if url_list is not set.
            additional_categories (Union[str, List[str]], optional): Used to configure or edit the additional categories of a \
            custom application / site used in the Application and URL Filtering or Threat Prevention.
            description (str, optional): 	A description for the application.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            urls_defined_as_regular_expression (bool, optional): States whether the URL is defined as a Regular Expression \
            or not. Defaults to False.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>>  firewallManagement.service_applications.application_site.add(
            ... name="New Application Site 1",
            ... tags=["t1"],
            ... comments="",
            ... additional_categories=[],
            ... application_id=15874256,
            ... application_signature="",
            ... description="A custom description",
            ... groups=[
            ...     {
            ...         "folder": {
            ...             "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
            ...             "name": "/Global Objects",
            ...         },
            ...         "domain": {
            ...             "domain-type": "local domain",
            ...             "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            ...             "name": "SMC User",
            ...         },
            ...         "type": "service-group",
            ...         "name": "My Service Group1",
            ...         "uid": "70600af1-3e61-41e2-b031-d46b2a171f86",
            ...     },
            ...     {
            ...         "folder": {
            ...             "uid": "5568324a-68ed-4c6c-9aa6-553978c7e746",
            ...             "name": "/Global Objects",
            ...         },
            ...         "domain": {
            ...             "domain-type": "local domain",
            ...             "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            ...             "name": "SMC User",
            ...         },
            ...         "type": "service-group",
            ...         "name": "My Service Group2",
            ...         "uid": "e971be7e-8372-475f-9863-c0b0c5285cc0",
            ...     },
            ... ],
            ... primary_category="",
            ... risk="",
            ... url_list=["www.4dz84zd39f9az26rh4hz64.com"],
            ... urls_defined_as_regular_expression=False,
            ... user_defined=True)
        """

        # Main request parameters
        payload = {"name": name, "primary-category": primary_category}

        if url_list is not None:
            payload["url-list"] = url_list
        elif application_signature is not None:
            payload["application-signature"] = application_signature
        else:
            raise MandatoryFieldMissing("url_list or application_signature")

        if description is not None:
            payload["description"] = description
        if additional_categories is not None:
            payload["additional-categories"] = additional_categories
        if tags is not None:
            payload["tags"] = tags
        if urls_defined_as_regular_expression is not None:
            payload[
                "urls-defined-as-regular-expression"
            ] = urls_defined_as_regular_expression

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("add-application-site", json=payload)

    def show(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Retrieve existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> FirewallManagement.service_applications.application_site.show(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.show_object(
            endpoint="show-application-site", uid=uid, name=name, **kw
        )

    def set(
        self,
        uid: str = None,
        name: str = None,
        new_name: str = None,
        primary_category: str = None,
        url_list: Union[str, List[str]] = None,
        application_signature: Union[str, List[str]] = None,
        additional_categories: Union[str, List[str]] = None,
        description: str = None,
        tags: Union[str, List[str]] = None,
        urls_defined_as_regular_expression: bool = False,
        **kw,
    ) -> Box:
        """
        Edit existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.
            new_name (str, optional): New name of the object.
            primary_category (str, optional): Each application is assigned to one primary category based on its most defining \
            aspect.
            url_list (Union[str, List[str]], optional): URLs that determine this particular application. Mandatory if
            application_signature is not set.
            application_signature (Union[str, List[str]], optional): Application signature generated by Signature Tool. \
            Mandatory if url_list is not set.
            additional_categories (Union[str, List[str]], optional): Used to configure or edit the additional categories of \
            a custom application / site used in the Application and URL Filtering or Threat Prevention.
            description (str, optional): 	A description for the application.
            tags (Union(str,List[str]), optional): Collection of tag identifiers.
            urls_defined_as_regular_expression (bool, optional): States whether the URL is defined as a Regular Expression \
            or not.

        Keyword Args:
            **color (Color, optional):
                Color of the object. Should be one of existing colors.
            **comments (str, optional):
                Comments string.
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **groups (Union(str,List[str]), optional):
                Collection of group identifiers.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> firewallManagement.service_applications.application_site.set(
            ... name="New Application Site 1",
            ... primary_category="Anonymizer",
            ... application_signature="^games\\.yahoo\\.com$")
        """

        # Main request parameters
        payload = {}
        if uid is not None:
            payload["uid"] = uid
        elif name is not None:
            payload["name"] = name
        else:
            raise MandatoryFieldMissing("uid or name")

        if url_list is not None:
            payload["url-list"] = url_list
        elif application_signature is not None:
            payload["application-signature"] = application_signature

        if new_name is not None:
            payload["new-name"] = new_name
        if primary_category is not None:
            payload["primary-category"] = primary_category
        if description is not None:
            payload["description"] = description
        if additional_categories is not None:
            payload["additional-categories"] = additional_categories
        if tags is not None:
            payload["tags"] = tags
        if urls_defined_as_regular_expression is not None:
            payload[
                "urls-defined-as-regular-expression"
            ] = urls_defined_as_regular_expression

        # Secondary parameters
        secondary_parameters = {
            "color": Color,
            "comments": str,
            "details-level": str,
            "groups": Union[str, List[str]],
            "ignore-warnings": bool,
            "ignore-errors": bool,
        }
        payload.update(sanitize_secondary_parameters(secondary_parameters, **kw))

        return self._post("set-application-site", json=payload)

    def delete(self, uid: str = None, name: str = None, **kw) -> Box:
        """
        Delete existing object using object name or uid.

        Args:
            uid (str, optional): Object unique identifier.
            name (str, optional): Object name.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **ignore-warnings (bool, optional):
                Apply changes ignoring warnings. Defaults to False
            **ignore-errors (bool, optional):
                Apply changes ignoring errors. You won't be able to publish such a changes.
                If ignore-warnings flag was omitted - warnings will also be ignored. Defaults to False

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> FirewallManagement.service_applications.application_site.delete(uid="ed997ff8-6709-4d71-a713-99bf01711cd5")
        """
        return self.delete_object(
            endpoint="delete-application-site", uid=uid, name=name, **kw
        )

    def show_application_sites(
        self,
        filter_results: str = None,
        limit: int = 50,
        offset: int = 0,
        order: List[dict] = None,
        **kw,
    ) -> Box:
        """
        Retrieve all objects.

        Args:
            filter_results (str, optional): Search expression to filter objects by.\
            The provided text should be exactly the same as it would be given in SmartConsole Object Explorer.\
            The logical operators in the expression ('AND', 'OR') should be provided in capital letters.\
            he search involves both a IP search and a textual search in name, comment, tags etc.
            limit (int, optional): The maximal number of returned results. Defaults to 50 (between 1 and 500)
            offset (int, optional): Number of the results to initially skip. Defaults to 0
            order (List[dict], optional): Sorts results by the given field. By default the results are sorted in the \
            descending order by the session publish time.
            show_as_ranges (bool, optional): When true, the group's matched content is displayed as ranges of IP addresses \
            rather than network objects. Objects that are not represented using IP addresses are presented as objects.\
            The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.\
            Defaults to False.

        Keyword Args:
            **details-level (str, optional):
                The level of detail for some of the fields in the response can vary from showing only the UID value\
                of the object to a fully detailed representation of the object.
            **domains-to-process (List[str], optional):
                Indicates which domains to process the commands on. It cannot be used with the details-level full,\
                must be run from the System Domain only and with ignore-warnings true.\
                Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.
            **show-membership (bool, optional):
                Indicates whether to calculate and show "groups" field for every object in reply.

        Returns:
            :obj:`Box`: The response from the server

        Examples:
            >>> FirewallManagement.service_applications.application_site.shows_application_sites()
        """
        return self.show_objects(
            endpoint="show-application-sites",
            filter_results=filter_results,
            limit=limit,
            offset=offset,
            order=order,
            extra_secondary_parameters={
                "show-membership": bool,
                "domains-to-process": List[str],
            },
            **kw,
        )
