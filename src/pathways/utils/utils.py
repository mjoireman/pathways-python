import semantic_version
import pkg_resources

def check_package(pkg_name, spec='*', is_optional=False):
    try:
        spec_pattern = semantic_version.SimpleSpec(spec)
        pkg_version = pkg_resources.get_distribution(pkg_name).version
        version = semantic_version.Version(pkg_version)
        if not spec_pattern.match(version):
            raise Exception('Package "{0}" version ({1}) does not match "{2}" '.format(pkg_name, version, spec) +
                            'Please run: pip install -U {0}'.format(pkg_name))
    except pkg_resources.DistributionNotFound:
        if is_optional:
            raise Exception('Optional package "{0}" is not installed. '.format(pkg_name) +
                            'Please run: pip install {0}'.format(pkg_name))
        else:
            raise Exception('Package "{0}" is not installed. '.format(pkg_name) +
                            'Please run: pip install {0}'.format(pkg_name))