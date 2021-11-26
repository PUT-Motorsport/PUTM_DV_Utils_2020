# PUT Motorsport Driverless ROS launch file as a Linux service
Setup of roslaunch file to run as a Linux system service. The roslaunch will start running shortly after operating system startup.

## Service files

**dv.service** - the service implementaion.
<br/>

**dv_startup.sh** - service executive script, contains:
- intitialization commands, 
- sourcing environment (ROS, workspace package) variables,
- configuration of camera sensor,
- run of roslaunch file.

## Configuration

1. Service file should be in `/lib/systemd/system/dv.service`.
2. Service executive script should be located in `/usr/bin/dv_startup.sh`.
3. Make `dv_startup.sh` executable with command `sudo chmod +x /usr/bin/dv_startup.sh`.
4. Enable `dv.service` by `sudo systemctl enable dv.service`.
5. Start service via `sudo systemctl start dv.service`.

## Useful systemctl commands

**restart** - restart a service. 
```bash
sudo systemctl restart dv.service
```

**stop** - stop a service. 
```bash
sudo systemctl stop dv.service
```

**status** - allow to check the status of service and also error output message. 
```bash
sudo systemctl status dv.service
```

Different useful commands are described [here](https://askubuntu.com/a/19324).