# -*- coding: utf-8 -*-
from drivers.replication_topologies.base import STOP_RESIZE_START
from drivers.replication_topologies.mysql_single import MySQLSingle
from drivers.tests.test_replication_topologies import AbstractReplicationTopologySettingsTestCase


class TestMySQLSingleSettings(AbstractReplicationTopologySettingsTestCase):

    def _get_replication_topology_driver(self):
        return MySQLSingle()

    def _get_deploy_settings(self):
        return (
            'workflow.steps.util.deploy.build_databaseinfra.BuildDatabaseInfra',
            'workflow.steps.mysql.deploy.create_virtualmachines.CreateVirtualMachine',
            'workflow.steps.mysql.deploy.create_secondary_ip.CreateSecondaryIp',
            'workflow.steps.mysql.deploy.create_dns.CreateDns',
            'workflow.steps.util.deploy.create_nfs.CreateNfs',
            'workflow.steps.mysql.deploy.create_flipper.CreateFlipper',
            'workflow.steps.mysql.deploy.init_database.InitDatabase',
            'workflow.steps.util.deploy.config_backup_log.ConfigBackupLog',
            'workflow.steps.util.deploy.check_database_connection.CheckDatabaseConnection',
            'workflow.steps.util.deploy.check_dns.CheckDns',
            'workflow.steps.util.deploy.create_zabbix.CreateZabbix',
            'workflow.steps.util.deploy.start_monit.StartMonit',
            'workflow.steps.util.deploy.create_dbmonitor.CreateDbMonitor',
            'workflow.steps.util.deploy.build_database.BuildDatabase',
            'workflow.steps.util.deploy.create_log.CreateLog',
            'workflow.steps.util.deploy.check_database_binds.CheckDatabaseBinds',
        )

    def _get_clone_settings(self):
        return self._get_deploy_settings() + (
            'workflow.steps.util.clone.clone_database.CloneDatabase',
            'workflow.steps.util.resize.check_database_status.CheckDatabaseStatus',
        )

    def _get_resize_settings(self):
        return (
            ('workflow.steps.util.volume_migration.stop_database.StopDatabase',
             'workflow.steps.mysql.resize.change_config.ChangeDatabaseConfigFile',
             ) + STOP_RESIZE_START +
            ('workflow.steps.util.resize.start_database.StartDatabase',
             'workflow.steps.util.resize.start_agents.StartAgents',
             'workflow.steps.util.resize.check_database_status.CheckDatabaseStatus',)
        )
