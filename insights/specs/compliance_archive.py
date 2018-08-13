from functools import partial
from insights.specs import Specs
from insights.core.context import HostArchiveContext
from insights.core.spec_factory import simple_file

simple_file = partial(simple_file, context=HostArchiveContext)


class ComplianceArchiveSpecs(Specs):

    arf_report = simple_file('/var/lib/insights/latest-compliance-results.xml')
    html_report = simple_file('/var/lib/insights/latest-compliance-results.html')
