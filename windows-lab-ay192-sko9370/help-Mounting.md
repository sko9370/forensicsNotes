
## Mounting image files in Windows
- Use `Arsenal Image Mounter` to mount most any type.
- FTK Imager can explore images as well as mount them as external drives.

## Mounting image files in linux 

1. Create an alias (e.g. add to `~/.bash_aliases`)

`alias mountwin='sudo mount -o ro,loop,show_sys_files,streams_interface=windows'`

- This can be used to mount an attached windows partition:  

`$ mountwin /dev/sdb1 /mnt/windows_mount0`  

- Unmount the partition when finished.

`$ umount /mnt/windows_mount0`

### Mounting a raw image file

- Determine the partitions and offsets (if a full disk image)  

`$ mmls /cases/DataLeakageCase/cfreds_2015_data_leakage_pc.dd`

- Use the `mountwin` command with additional options specifying an offset  

```
$ mountwin -o offset=$((512 * 206848)) /cases/DataLeakageCase/cfreds_2015_data_leakage_pc.dd /mnt/windows_mount
```

### Mounting a Volume Shadow copy
- Determine the NTFS partition and offset

`$ mmls /cases/DataLeakageCase/cfreds_2015_data_leakage_pc.dd`

- Determine if a VSC exists

`$ vshadowinfo -o $((512 * 206848)) /cases/DataLeakageCase/cfreds_2015_data_leakage_pc.dd`

- Mount the VSC (mounted at /mnt/vss/vss1)

`$ vshadowmount -o $((512 * 206848)) /cases/DataLeakageCase/cfreds_2015_data_leakage_pc.dd /mnt/vss`

- Mount the VSC as a Window partition ( mounted at /mnt/shadow/vss1/ )

`$ mountwin /mnt/vss/vss1 /mnt/shadow/vss1`
