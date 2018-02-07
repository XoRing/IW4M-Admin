﻿
using SharedLibrary.Database.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace StatsPlugin.Models
{
    public class EFServer : SharedEntity
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int ServerId { get; set; }
        [Required]
        public int Port { get; set; }
    }
}
