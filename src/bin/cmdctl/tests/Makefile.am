PYCOVERAGE_RUN=@PYCOVERAGE_RUN@
PYTESTS = cmdctl_test.py bundy-certgen_test.py
EXTRA_DIST = $(PYTESTS)
EXTRA_DIST += testdata/expired-certfile.pem
EXTRA_DIST += testdata/mangled-certfile.pem
EXTRA_DIST += testdata/noca-certfile.pem

# If necessary (rare cases), explicitly specify paths to dynamic libraries
# required by loadable python modules.
LIBRARY_PATH_PLACEHOLDER =
if SET_ENV_LIBRARY_PATH
LIBRARY_PATH_PLACEHOLDER += $(ENV_LIBRARY_PATH)=$(abs_top_builddir)/src/lib/cryptolink/.libs:$(abs_top_builddir)/src/lib/dns/.libs:$(abs_top_builddir)/src/lib/dns/python/.libs:$(abs_top_builddir)/src/lib/cc/.libs:$(abs_top_builddir)/src/lib/config/.libs:$(abs_top_builddir)/src/lib/log/.libs:$(abs_top_builddir)/src/lib/util/.libs:$(abs_top_builddir)/src/lib/util/threads/.libs:$(abs_top_builddir)/src/lib/exceptions/.libs:$(abs_top_builddir)/src/lib/util/io/.libs:$(abs_top_builddir)/src/lib/datasrc/.libs:$$$(ENV_LIBRARY_PATH)
endif

CLEANFILES = test-keyfile.pem test-certfile.pem

# test using command-line arguments, so use check-local target instead of TESTS
check-local:
if ENABLE_PYTHON_COVERAGE
	touch $(abs_top_srcdir)/.coverage
	rm -f .coverage
	${LN_S} $(abs_top_srcdir)/.coverage .coverage
endif
	for pytest in $(PYTESTS) ; do \
	echo Running test: $$pytest ; \
	$(LIBRARY_PATH_PLACEHOLDER) \
	PYTHONPATH=$(COMMON_PYTHON_PATH):$(abs_top_builddir)/src/bin/cmdctl \
	CMDCTL_SRC_PATH=$(abs_top_srcdir)/src/bin/cmdctl \
	CMDCTL_BUILD_PATH=$(abs_top_builddir)/src/bin/cmdctl \
	BUNDY_LOCKFILE_DIR_FROM_BUILD=$(abs_top_builddir) \
	$(PYCOVERAGE_RUN) $(abs_srcdir)/$$pytest || exit ; \
	done
