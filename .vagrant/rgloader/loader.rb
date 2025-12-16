

if ENV["VAGRANT_INSTALLER_EMBEDDED_DIR"]
  require File.expand_path(
    "rgloader/loader", ENV["VAGRANT_INSTALLER_EMBEDDED_DIR"])
else
  raise "Encoded files can't be read outside of the Vagrant installer."
end
