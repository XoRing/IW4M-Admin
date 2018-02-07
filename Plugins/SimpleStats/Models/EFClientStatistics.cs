﻿using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using SharedLibrary.Database.Models;

namespace StatsPlugin.Models
{
    public class EFClientStatistics : SharedEntity
    {
        [Key, Column(Order = 0)]
        public int ClientId { get; set; }
        [ForeignKey("ClientId")]
        public virtual EFClient Client { get; set; }
        [Key, Column(Order = 1)]
        public int ServerId { get; set; }
        [ForeignKey("ServerId")]
        public virtual EFServer Server { get; set; }
        [Required]
        public int Kills { get; set; }
        [Required]
        public int Deaths { get; set; }
        [Required]
        [NotMapped]
        public double KDR
        {
            get => Deaths == 0 ? 0.0 : Math.Round((float)Kills / (float)Deaths, 2);
        }
        [Required]
        public double SPM { get; set; }
        [Required]
        public double Skill { get; set; }
    }
}
