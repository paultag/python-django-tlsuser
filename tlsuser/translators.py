from cryptography import x509
from cryptography.x509.oid import NameOID, ExtensionOID


class ExampleTranslator(object):
    def get_username(self, cert):
        # common_names = [x.value for x in cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)]
        emails = cert.extensions.get_extension_for_oid(
            ExtensionOID.SUBJECT_ALTERNATIVE_NAME,
        ).value.get_values_for_type(
            x509.RFC822Name,
        )
        if len(emails) == 0:
            return None
        return emails[0]
