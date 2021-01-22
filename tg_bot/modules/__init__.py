from tg_bot import LOAD, NO_LOAD, LOGGER

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NO_LOAD:
        to_load = LOADto_load = all_modules

        if NO_LOAD:
            LOGGER.info(" {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGGEad: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
